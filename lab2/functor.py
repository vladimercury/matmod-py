from lab2.chebyshev import chebyshev_function


def get_polynom_counter(polynom):
    def f(x):
        y = 0
        for i in polynom:
            y += (x ** i) * polynom[i]
        return y
    return f


def get_chebyshev_counter(coefficients, x_to_u):
    n = len(coefficients)
    def f(x):
        u = x_to_u(x)
        cheb = chebyshev_function(u, n)
        res = 0
        for i in range(0, n):
            res += coefficients[i] * cheb[i]
        return res
    return f


def get_interval_transformer(a, b):
    c = (a + b) / 2.0
    d = (b - a) / 2.0

    def get_u(x):
        return (x - c) / d

    def get_x(u):
        return d * u + c

    return get_u, get_x