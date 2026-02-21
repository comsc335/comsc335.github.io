(notation_catalog)=

# Notation catalog

```{list-table}
:header-rows: 1
:widths: 25 75

* - Notation
  - Meaning
* - $i = 1, 2, \ldots, n$
  - Index of an example in the dataset
* - $(\quad)$
  - Parentheses indicate an ordered set of elements (a **tuple**)
* - $(\vec{x}_i, y_i)$
  - Ordered pair of a data example and its answer/label
* - $j = 1, 2, \ldots, p$
  - Index of a **feature** in a data example
* - $\vec{x} = (x_1, x_2, \ldots, x_p)$
  - A **vector** with $p$ features $(x_1, x_2, \ldots, x_p)$
* - $\vec{x}_i = (x_{i,1}, x_{i,2}, \ldots, x_{i,p})$
  - A **vector** with $p$ features $(x_{i,1}, x_{i,2}, \ldots, x_{i,p})$ for the $i$-th data example
* - $f(\vec{x})$
  - A function that takes in a data example $\vec{x}$ and outputs a prediction $\hat{y}$
* - $\hat{y}$
  - A **prediction** (we want this to be close to the true answer)
* - $\mathcal{L}(\vec{w})$
  - A **loss function**, a function of the weights $\vec{w} = (w_0, w_1, \ldots, w_p)$, which quantifies the error of the model
* - $\nabla \mathcal{L}(\vec{w})$ = $\left(\frac{\partial \mathcal{L}}{\partial w_0}, \frac{\partial \mathcal{L}}{\partial w_1}, \ldots, \frac{\partial \mathcal{L}}{\partial w_p}\right)$
  - The **gradient** of $\mathcal{L}(\vec{w})$ with respect to the weights $\vec{w}$, a vector of partial derivatives
* - $\ell_i$
  - The loss function calculated for a single data example $(\vec{x}_i, y_i)$
* - $\sigma(h) = \frac{1}{1 + e^{-h}}$
  - The **sigmoid** function (also called the logistic function), a function that takes in a linear combination of features $h$ and outputs a probability in the range $(0, 1)$
```