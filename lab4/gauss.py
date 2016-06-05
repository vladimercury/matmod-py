from fractions import Fraction


def gauss(a, b):
    n = len(b)
    x = [Fraction(0) for i in range(n)]
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= a[i][j] * x[j]
        x[i] /= a[i][i]
    return x