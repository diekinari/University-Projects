def sum_vectors(args):
    x = 0
    y = 0
    z = 0
    for i in range(len(args)):
        x += args[i][0]
        y += args[i][1]
        z += args[i][2]
    return (x, y, z)


def vector_times_digit(vector, digit):
    res = []
    for i in range(len(vector)):
        res.append(vector[i] * digit)
    return res


def find_min_and_max(vector):
    return [min(vector), max(vector)]
