def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # y = a*(x**2) + b*x + c

    # at time t , (t=0)
    x_t = x0 - lr*(2*a*x0 + b)

    for i in range(1, steps):
        x_t1 = x_t - lr*(2*a*x_t + b)
        x_t = x_t1
    return x_t1