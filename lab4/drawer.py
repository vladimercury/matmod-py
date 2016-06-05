def draw_graph(y):
    import matplotlib.pyplot as p
    x = range(len(y))
    p.figure()
    p.plot(x, y)
    p.show()