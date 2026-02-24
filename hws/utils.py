"""Utility functions for homeworks."""

import functools
import numpy as np
import seaborn as sns
import ipywidgets as widgets
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

########################################################
# Homework 1
########################################################
def minmax(X: np.ndarray) -> np.ndarray:
    """Normalize data to [0,1]"""
    X = np.asarray(X, dtype=float)
    mn = X.min(axis=0, keepdims=True)
    mx = X.max(axis=0, keepdims=True)
    return (X - mn) / (mx - mn + 1e-12)


def sim_data(n: int=90, noise: float=0.08, seed: int=7):
    """Two-regime mixture simulated data"""
    rng = np.random.default_rng(seed)
    n1 = n // 2
    n2 = n - n1

    # cluster A
    X_A = rng.normal(loc=[-1.0, 0.8], scale=[0.35, 0.35], size=(n1, 2))
    # cluster B
    X_B = rng.normal(loc=[1.0, -0.6], scale=[0.45, 0.45], size=(n2, 2))
    X_raw = np.vstack([X_A, X_B])
    X = minmax(X_raw)

    # Different linear rules by regime (misspecified if you fit one linear model)
    yA = 0.2 + 2.6 * X[:n1, 0] - 2.0 * X[:n1, 1]
    yB = 0.6 - 1.2 * X[n1:, 0] + 2.4 * X[n1:, 1]
    y = np.concatenate([yA, yB]) + rng.normal(0, noise, size=n)

    # Shuffle so regimes are mixed
    perm = rng.permutation(n)
    return X[perm], y[perm]


def gradnorm_grid(X, y, w1_grid, w2_grid):
    """Compute the gradient norm over a grid of (w1,w2) values, with w0 profiled out"""
    x1 = X[:, 0]
    x2 = X[:, 1]
    n = X.shape[0]
    x1c = x1 - x1.mean()
    x2c = x2 - x2.mean()
    yc  = y  - y.mean()

    W1, W2 = np.meshgrid(w1_grid, w2_grid)
    grad = np.zeros_like(W1, dtype=float)
    loss = np.zeros_like(W1, dtype=float)

    for i in range(W1.shape[0]):
        for j in range(W1.shape[1]):
            w1 = W1[i, j]
            w2 = W2[i, j]
            r = w1 * x1c + w2 * x2c - yc
            loss[i, j] = np.mean(r**2)
            g1 = (2.0 / n) * np.sum(r * x1c)
            g2 = (2.0 / n) * np.sum(r * x2c)
            grad[i, j] = np.sqrt(g1**2 + g2**2)

    return W1, W2, loss, grad


def explore_alpha(LinModel, alpha: float):
    """Simulation for exploring the effect of alpha on the gradient descent algorithm.
    
    Args:
        LinModel: the linear regression model to use
        alpha: the learning rate

    Returns:
        None
    """
    # Fix the data seed for HW 1 exercise
    data_seed = 7

    X, y = sim_data(n=90, noise=0.08, seed=data_seed)
    #X, y = TOYS[toy](seed=data_seed)

    np.random.seed(data_seed)
    model = LinModel(alpha=alpha).fit(X, y)

    w1_hist = np.array([w[1] for w in model.w_history_])
    w2_hist = np.array([w[2] for w in model.w_history_])
    T = len(w1_hist)

    # Show intermediate dots every 50 or 100 iterations
    stride = 1 # if T <= 1000 else 100
    idx = np.arange(0, T, stride)

    w1_min, w1_max = w1_hist.min(), w1_hist.max()
    w2_min, w2_max = w2_hist.min(), w2_hist.max()

    pad1 = 0.15 * (w1_max - w1_min + 1e-6)
    pad2 = 0.15 * (w2_max - w2_min + 1e-6)

    w1_grid = np.linspace(w1_min - pad1, w1_max + pad1, 180)
    w2_grid = np.linspace(w2_min - pad2, w2_max + pad2, 180)
    W1, W2, Loss, Grad = gradnorm_grid(X, y, w1_grid, w2_grid)


    fig, ax = plt.subplots(1, 1, figsize=(7.6, 5.2))

    cf = ax.contourf(W1, W2, Loss, levels=22, cmap="viridis")
    c = ax.contour(W1, W2, Loss, levels=12, colors="white", linewidths=0.8, alpha=0.75)
    ax.clabel(c, inline=True, fontsize=8, fmt="%.2f")

    ax.plot(w1_hist, w2_hist, color="tomato", linewidth=1, alpha=0.85)
    ax.scatter(w1_hist[idx], w2_hist[idx], s=10, color="white", edgecolor="white",
                  linewidth=0.6, alpha=0.5)
    # , label=f"every {stride} iters"
    ax.scatter(w1_hist[0], w2_hist[0], s=70, color="white", edgecolor="black", zorder=5, label="start")
    ax.scatter(w1_hist[-1], w2_hist[-1], s=85, color="tomato", edgecolor="black", zorder=5, label="end")

    iterations = len(model.loss_values_)
    final_mse = float(model.loss_values_[-1])
    max_iters = getattr(model, "max_iters", None)
    hit_iter_limit = (max_iters is not None) and (iterations >= max_iters)

    if hit_iter_limit:
        title = f"MSE loss contours: {max_iters} iteration limit reached | final MSE={final_mse:.4f}"
    else:
        title = f"MSE loss contours: converged in {iterations} iterations | final MSE={final_mse:.4f}"

    ax.set_title(title)
    ax.set_xlabel(r"$w_1$")
    ax.set_ylabel(r"$w_2$")
    ax.legend(frameon=True, loc="upper right")
    fig.colorbar(cf, ax=ax, label="MSE")

    ax.set_xlim(w1_grid.min(), w1_grid.max())
    ax.set_ylim(w2_grid.min(), w2_grid.max())

    plt.tight_layout()
    display(fig)
    plt.close(fig)

    print(
        f"alpha={alpha:.2f} | iters={len(model.loss_values_)} | "
        f"final [w0,w1,w2]={model.weights_} | final MSE={model.loss_values_[-1]:.4f}"
    )

########################################################
# Homework 2
########################################################


def explore_categorical_errors(df, column_name, error_type):
    """Display false positive or false negative rates by categorical column"""
    
    # Calculate rates for each category value
    rates_data = []
    
    for category_value in df[column_name].unique():
        # Filter data for this category value
        category_mask = df[column_name] == category_value
        category_data = df[category_mask]
        
        # Calculate total positives and negatives for this category
        total_actual_pos = (category_data['income_>50k'] == 1).sum()
        total_actual_neg = (category_data['income_>50k'] == 0).sum()
        
        # Calculate false positives and false negatives for this category
        false_pos_count = (category_data['false_pos'] == 1).sum()
        false_neg_count = (category_data['false_neg'] == 1).sum()
        
        # Calculate rates (avoid division by zero)
        fpr = (false_pos_count / total_actual_neg * 100) if total_actual_neg > 0 else 0
        fnr = (false_neg_count / total_actual_pos * 100) if total_actual_pos > 0 else 0
        
        # Select which rate to display based on error_type
        if error_type == 'False Positive Rate (%)':
            rate_value = round(fpr, 1)
        else:  # False Negative Rate (%)
            rate_value = round(fnr, 1)
        
        rates_data.append({
            'Category': category_value,
            error_type: rate_value,
        })
    
    # Create dataframe and sort by total count (most common categories first)
    rates_df = pd.DataFrame(rates_data)
    rates_df = rates_df.sort_values(error_type, ascending=False)

    print(f"\n{error_type} of the best model by {column_name}:")
    # print("=" * 80)
    # if error_type == 'False Positive Rate (%)':
    #     print("False Positive Rate = False Positives / Total Actual Negatives")
    # else:
    #     print("False Negative Rate = False Negatives / Total Actual Positives")
    # print()
    display(rates_df.reset_index(drop=True))