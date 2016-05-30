def chebyshev_coefficients(u, y):
    num = len(y)
    cheb = [chebyshev_function(t, num) for t in u]
    coef_array = [0] * num
    for i in range(0, num):
        coef = 0
        for j in range(0, num):
            coef += cheb[j][i] * y[j]
        coef_array[i] = 2 * coef / num
    coef_array[0] /= 2
    return coef_array


def chebyshev_function(x, n):
    res = [1.0, 1.0*x]
    if n < 3:
        return [res[t] for t in range(0, n)]
    res += [0] * (n-2)
    for t in range(2, n):
        res[t] = 2.0 * x * res[t-1] - res[t-2]
    return res


def chebyshev_nodes(n):
    from math import cos, pi
    return [cos((2*i-1)*pi/(2.0*n)) for i in range(1, n+1)]


