def chebyshev_approximation(function, int_start, int_end, num_of_nodes, only_relative_error=False):
    from lab2 import drawer
    from lab2.chebyshev import chebyshev_nodes, chebyshev_coefficients
    from lab2.functor import get_interval_transformer, get_chebyshev_counter
    from lab2.util import array_sort, array_round
    get_u, get_x = get_interval_transformer(int_start, int_end)
    u = array_sort(chebyshev_nodes(num_of_nodes))
    print("Nodes: " + str(array_round(u, 6)))
    x = [get_x(t) for t in u]
    y = [function(t) for t in x]
    c = chebyshev_coefficients(u, y)
    print("Chebyshev coefficients:")
    [print(("c%-2d" % i) + (" =  %+.10f" % c[i])) for i in range(0, len(c))]
    f2 = get_chebyshev_counter(c, get_u)
    drawer.draw_approx_error_plot(function, [f2], int_start, int_end, onlyrelative=only_relative_error)