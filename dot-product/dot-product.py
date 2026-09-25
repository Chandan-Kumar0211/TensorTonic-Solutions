import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    dot = 0
    for i in range(len(x)):
        dot += x[i] * y[i]

    return float(dot)