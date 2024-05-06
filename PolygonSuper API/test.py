from polygonSuper import *


# task 1
# polygons_iterator = [((0, 0), (1, 0), (1, 1)), ((1, 1), (2, 1), (2, 2)), ((2, 2), (3, 2), (3, 3)),
#                      ((0, 3), (1, 2), (0, 2)), ((1, 2), (2, 1), (1, 1)), ((2, 1), (3, 0), (2, 0))]
# visualize_polygons(polygons_iterator)


# task 2
# gen_r(limit=100)
# gen_triangle(100)
# gen_hexagon(100, 0.5)
# generate_random_figures()

# task 3
# polygons = gen_rectangle(limit=5, visualize=False)
# polygons = gen_hexagon(5, vizualize=False, side_length=1)
# print(polygons)

# -- usage example 1 (use 'lambda polygon: func(polygon, arg)' in case of requiring a specific output) --
# $ polygon translation
# polygons = map(tr_translate, polygons)

# $ polygon rotation
# polygons = map(tr_rotate, polygons)

# $ polygon symmetry(for more clearly view see u.e. 2)
# polygons = map(tr_symmetry, polygons)

# $ polygon homothety
# polygons = map(tr_homothety, polygons)

# visualize_polygons(polygons)

# -- -- --

# usage example 2
# new_polygons = []
# for polygon in polygons:
# new_polygons.append(tr_translate(polygon, (2, 2)))

# new_polygons.append(tr_rotate(polygon, 90))

# new_polygons.append(tr_rotate(tr_symmetry(polygon, 'y')))

# new_polygons.append(tr_homothety(polygon, 2))

# visualize_polygons(new_polygons)

# result = tuple(new_polygons) + tuple(map(tr_rotate, gen_rectangle(limit=5, visualize=False)))
# visualize_polygons(result)

# task 4
# -- graphic 1 --
# top_line = map(lambda polygon:
#                tr_rotate(polygon, 30),
#                tuple(map(lambda polygon:
#                          tr_translate(polygon, (-10, 1.5)),
#                          gen_rectangle(8, (2, 1, 1, 2), False))))
#
# mid_line = map(lambda polygon:
#                tr_rotate(polygon, 30),
#                tuple(map(lambda polygon:
#                          tr_translate(polygon, (-10, 0)),
#                          gen_rectangle(8, (2, 1, 1, 2), False))))
# bottom_line = map(lambda polygon:
#                   tr_rotate(polygon, 30),
#                   tuple(map(lambda polygon:
#                             tr_translate(polygon, (-10, -1.5)),
#                             gen_rectangle(8, (2, 1, 1, 2), False))))
# visualize_polygons(tuple(top_line) + tuple(mid_line) + tuple(bottom_line))

# -- graphic 2 --
# topline = map(lambda polygon: tr_rotate(polygon, 320),
#               tuple(map(lambda polygon:
#                         tr_translate(polygon, (-8, 5)),
#                         gen_rectangle(8, (2, 1, 1, 2), False))))
# bottomline = map(lambda polygon: tr_rotate(polygon, 30),
#                  tuple(map(lambda polygon:
#                            tr_translate(polygon, (-2, 0)),
#                            gen_rectangle(8, (2, 1, 1, 2), False))))
# visualize_polygons(tuple(topline) + tuple(bottomline))

# -- graphic 3 --
# slightly left and down
# topline = map(lambda polygon: tr_symmetry(polygon),
#               tuple(map(lambda polygon:
#                         tr_translate(polygon, (-5, -2.5)),
#                         gen_triangle(7, 1, False))))
# # just left
# bottomline = map(lambda polygon:
#                  tr_translate(polygon, (-5, 0)),
#                  gen_triangle(7, 1, False))
# visualize_polygons(tuple(topline) + tuple(bottomline))

# -- graphic 4 --

def rotate(element, angle):
    return tuple(map(lambda polygon: tr_rotate(polygon, angle), tuple(element)))


def move(element, vector):
    return tuple(map(lambda polygon: tr_translate(polygon, vector), tuple(element)))


def sym(element, axis):
    return tuple(map(lambda polygon: tr_symmetry(polygon, axis), tuple(element)))


#
#
# polygons = []
# first_el = gen_trapezoid(1, side_lengths=(1.5, 1.2, 1.5, 1.2), angles=(120, 120), visualize=False)
# second_el = gen_trapezoid(1, side_lengths=(2.9, 1.25, 2.9, 1.25), angles=(120, 120), start_x=5, visualize=False)
# third_el = gen_trapezoid(1, side_lengths=(4.9, 1.8, 4.9, 1.8), angles=(120, 120), start_x=10, visualize=False)
# fourth_el = gen_trapezoid(1, side_lengths=(6.9, 1.9, 6.9, 1.9), angles=(120, 120), start_x=10, visualize=False)
#
# polygons.append(rotate(move(move(rotate(first_el, 90), (2.6, 0))
#                             + move(rotate(second_el, 90), (4, -5.7))
#                             + move(rotate(third_el, 90), (6, -11.7))
#                             + move(rotate(fourth_el, 90), (8.1, -12.7)),
#                             (-1.2, -0.8)), 45))
#
# polygons.append(sym(sym(polygons[0], axis='y'), axis='x'))
#
# visualize_polygons(polygons[0] + polygons[1])

# task 5
rects = gen_rectangle(3, (2, 1, 1, 2), False)
rects2 = gen_trapezoid(2, (1, 5, 10, 5), (120, 120), visualize=False)
polygons = move(rects, (6, 0)) + tuple(rects2)
filtered = filter(is_convex, polygons)
visualize_polygons(polygons)
visualize_polygons(list(filtered))
