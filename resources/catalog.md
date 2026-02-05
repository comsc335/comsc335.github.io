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
* - $f(\vec{x})$
  - A function that takes in a data example $\vec{x}$ and outputs a prediction $\hat{y}$
* - $\hat{y}$
  - A **prediction** (we want this to be close to the true answer)
* - $\mathcal{L}(\vec{w})$
  - The loss function, a function of the weights $\vec{w} = (w_0, w_1, \ldots, w_k)$, which quantifies the error of the model
```