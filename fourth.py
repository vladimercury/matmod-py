from fractions import Fraction
from lab4.gauss import gauss

u = [[Fraction(1) if i == j else Fraction(-2) if i > j else Fraction(0) for j in range(32)] for i in range(32)]
b = [Fraction(1, 1) if i % 2 == 0 else Fraction(-1, 3) for i in range(32)]
x = gauss(u, b)
x_dbl = [i.numerator / i.denominator for i in x]

ud = [[1 if i == j else -2 if i > j else 0 for j in range(32)] for i in range(32)]
bd = [1 if i % 2 == 0 else -1/3 for i in range(32)]
xd = gauss(ud, bd)

d = [sum([ud[i][j] * xd[j] for j in range(32)]) - bd[i] for i in range(32)]
n = len(b)

delta_otn = [d[i] / bd[i] for i in range(n)]

[print(''.join(["%2s " % ud[i][j] for j in range(n)]\
               + [" | %4s" % b[i]]\
               + [" | %28s" % ("%.12f" % xd[i])]\
               + [" | %13s" % ("%.6e" % d[i])]\
               + [" | %13s " % ("%.6e" % delta_otn[i])])) for i in range(n)]

bdd = [d[i] + bd[i] for i in range(32)]
xdd = gauss(ud, bdd)
dd = [(xdd[i] - xd[i])/xd[i] for i in range(32)]

[print(''.join(["%2s " % ud[i][j] for j in range(n)] \
               + [" | %20s" % bdd[i]] \
               + [" | %28s" % ("%.12f" % xdd[i])] \
               + [" | %13s" % ("%.6e" % dd[i])])) for i in range(n)]