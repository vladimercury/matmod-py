def draw_graph(a, b, function, color='r', interval=100.0):
    import matplotlib.pyplot as p
    from numpy import arange
    xpoints = arange(a, b, (b-a)/interval)
    ypoints = [function(tpoint) for tpoint in xpoints]
    p.figure()
    p.plot(xpoints, ypoints)
    p.show()


def draw_approx_error_plot(f, approxlist, a, b, onlyrelative=False):
    import numpy as np
    import matplotlib.pyplot as p
    x = np.linspace(a, b, 1000)
    p.figure()
    p.plot(x, [f(t) for t in x])
    vfuncs = [np.vectorize(approx) for approx in approxlist]
    p.plot(x, [0 for t in x], color='r')
    for vf in vfuncs:
        p.plot(x, vf(x), color='k')
    p.xlim(a, b)
    p.ylabel('f(x) and approximations fa(x)')
    if not onlyrelative:
        p.figure()
        p.plot(x, [0 for t in x], color='r')
        for vf in vfuncs:
            p.plot(x, [f(t) - vf(t) for t in x])
        p.xlim(a, b)
        p.ylabel('error = f(x)-fa(x)')
        p.xlabel('x')
    p.figure()
    p.plot(x, [0 for t in x], color='r')
    for vf in vfuncs:
        p.plot(x, [(f(t) - vf(t)) / f(t) for t in x])
    p.xlim(a, b)
    p.ylabel('relative error')
    p.xlabel('x')
    p.show()
