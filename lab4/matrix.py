from fractions import Fraction

class Matrix:
    def __init__(self, *args):
        self.data = []
        self.x, self.y = 0, 0
        if len(args) == 1:
            a = args[0]
            if is_matrix(a):
                self.y = len(a)
                if self.y > 0:
                    self.x = len(a[0])
                self.data = [[0] * self.x for i in range(self.y)]
                for i in range(len(a)):
                    for j in range(len(a[i])):
                        self.data[i][j] = a[i][j]
            else:
                raise TypeError('a is not a matrix')
        elif len(args) == 2:
            self.x, self.y = args[0], args[1]
            self.data = [[0] * self.x for i in range(self.y)]
        elif len(args) == 3:
            self.x, self.y = args[0], args[1]
            self.data = [[args[2]] * self.x for i in range(self.y)]
        else:
            raise TypeError('__init__() takes exactly one or two arguments')

    def __mul__(self, other):
        if type(other) == Matrix:
            if self.x != other.y:
                raise ValueError("Width of a != height of b")
            c = [[0] * other.x for i in range(self.y)]
            for i in range(0, len(c)):
                for j in range(0, len(c[i])):
                    for k in range(0, self.x):
                        c[i][j] += self.data[i][k] * other.data[k][j]
            return Matrix(c)
        elif type(other) == int or type(other) == float:
            c = [[0] * self.x for i in range(self.y)]
            for i in range(0, len(c)):
                for j in range(0, len(c[i])):
                    c[i][j] = other * self.data[i][j]
            return Matrix(c)

    def __str__(self):
        max = 0
        for i in self.data:
            for j in i:
                if len(str(j)) >= max:
                    max = len(str(j))
                    if j >= 0:
                        max += 1
        fmt = "%" + str(max) + "s "
        return ''.join([''.join([fmt % str(j) for j in i]) + '\n' for i in self.data])

    def transp(self):
        c = [[0] * self.y for i in range(self.x)]
        for i in range(self.y):
            for j in range(self.x):
                c[j][i] = self.data[i][j]
        return Matrix(c)

    def is_triangle(self):
        up_not_null = True
        down_not_null = True
        for i in range(0, self.y - 1):
            for j in range(i + 1, self.x):
                if self.data[i][j] != 0:
                    up_not_null = False
                    break
            if not up_not_null:
                break
        for i in range(1, self.y):
            for j in range(0, i):
                if self.data[i][j] != 0:
                    down_not_null = False
                    break
            if not down_not_null:
                break
        return up_not_null or down_not_null

    def det_main_diag(self):
        res = 1
        for i in range(self.y):
            res *= self.data[i][i]
        return res

def is_matrix(a):
    # MATRIX VALIDATION
    # type validation
    if type(a) != list:
        return False
    n = len(a[0]) if len(a) > 0 else 0
    for x in a:
        if type(x) != list:
            return False
        if len(x) != n:
            return False
        for y in x:
            if type(y) != int and type(y) != float and type(y) != Fraction:
                return False
    return True