import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    x = np.asarray(x, dtype=float)
    num = 1
    deno = 1 + np.exp(-1*x)

    return num/deno