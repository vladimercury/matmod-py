from numpy import *
from numpy.linalg import cond

# generating a random overdetermined system
A = [[1 if i == j else -2 if i > j else 0 for j in range(32)] for i in range(32)]
b = [1 if i % 2 == 0 else -1/3 for i in range(32)]

x_lstsq = linalg.lstsq(A,b)[0] # computing the numpy solution

Q,R = linalg.qr(A) # qr decomposition of A
Qb = dot(Q.T,b) # computing Q^T*b (project b onto the range of A)
x_qr = linalg.solve(R,Qb) # solving R*x = Q^T*b

d = [sum([A[i][j] * x_qr[j] for j in range(32)]) - b[i] for i in range(32)]
n = len(b)

delta_otn = [d[i] / b[i] for i in range(n)]

[print(''.join(["%2s " % A[i][j] for j in range(n)] \
               + [" | %20s" % b[i]] \
               + [" | %28s" % ("%.6e" % x_qr[i])] \
               + [" | %13s" % ("%.6e" % d[i])] \
               + [" | %13s " % ("%.6e" % delta_otn[i])])) for i in range(n)]

d = [sum([A[i][j] * x_lstsq[j] for j in range(32)]) - b[i] for i in range(32)]
n = len(b)

print()
delta_otn = [d[i] / b[i] for i in range(n)]

[print(''.join(["%2s " % A[i][j] for j in range(n)]\
               + [" | %20s" % b[i]]\
               + [" | %28s" % ("%.6e" % x_lstsq[i])] \
               + [" | %13s" % ("%.6e" % d[i])] \
               + [" | %13s " % ("%.6e" % delta_otn[i])])) for i in range(n)]

print("QR")
print(cond(R))
print("Obr")
print(cond(A))