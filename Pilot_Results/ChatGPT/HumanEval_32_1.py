import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """Find and return one zero of the polynomial defined by xs."""
    left, right = -1.0, 1.0

    while poly(xs, left) * poly(xs, right) > 0:
        left *= 2
        right *= 2

    while right - left > 1e-10:
        mid = (left + right) / 2
        value = poly(xs, mid)

        if abs(value) < 1e-12:
            return mid

        if poly(xs, left) * value < 0:
            right = mid
        else:
            left = mid

    return (left + right) / 2