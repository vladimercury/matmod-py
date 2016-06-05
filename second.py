from lab2.approx import chebyshev_approximation
from math import log, e, exp

def ln(x):
    return log(x, e)

chebyshev_approximation(ln, 0.001, 5, 50, only_relative_error=False)
