from lab2.approx import chebyshev_approximation
from math import log, e


def ln(x):
    return log(x, e)

chebyshev_approximation(ln, 0.2, 5, 15, only_relative_error=False)
