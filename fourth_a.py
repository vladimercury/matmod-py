from numpy.linalg import det, cond
from lab2.drawer import draw_diag
from math import log, e


def ln(w):
    return log(w, e)

x = []
y = []
for n in range(1, 33):
    u = [[1 if i == j else -2 if i > j else 0 for j in range(n)] for i in range(n)]
    c = cond(u)
    x.append(n)
    y.append(c)
    print("%2d : det = %s u = %e" % (n, det(u), c))
z = [ln(t) for t in y]

draw_diag(x, y, title="f = u(n)", xlabel='n', ylabel='u (n)', color='r', show=False)
draw_diag(x, z, title="f = ln(u(n))", xlabel='n', ylabel='ln (u(n))', color='blue')