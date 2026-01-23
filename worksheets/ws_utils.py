"""Utility functions for worksheets."""

import functools
import numpy as np
import seaborn as sns
import ipywidgets as widgets
import matplotlib.pyplot as plt
from IPython.display import display
from sklearn.datasets import fetch_california_housing



########################################################
# Worksheet 1
########################################################

def explore_n_neighbors(KNNRegressor, n_neighbors: int):
    """Explore the effect of the number of neighbors on the KNN model.
    
    Args:
        KNNRegressor: the KNN regressor to use
        n_neighbors: the number of neighbors to use

    Returns:
        None
    """
    housing = fetch_california_housing()

    X_train = housing.data[:100, 0].reshape(-1, 1)
    y_train = housing.target[:100]

    model = KNNRegressor(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)

    xs = np.linspace(X_train[:, 0].min(), X_train[:, 0].max(), 100).reshape(-1, 1)
    ys = model.predict(xs)

    y_hat = model.predict(X_train)

    plt.figure(figsize=(6, 4))
    plt.xlim(0, 5)

    sns.scatterplot(x=X_train[:, 0], y=y_train, s=35, alpha=0.8, label="training data")
    sns.lineplot(x=xs[:, 0], y=ys, color="C1", linewidth=2, label="KNN prediction")
    plt.xlabel("Median income (tens of thousands of dollars)")
    plt.ylabel("House price (100k's)")
    plt.title(f"KNN regression fit (n_neighbors={n_neighbors})")
    plt.legend()
    plt.show()