def array_sort(array):
    array.sort()
    return array


def array_round(array, accuracy):
    return [round(x, accuracy) for x in array]