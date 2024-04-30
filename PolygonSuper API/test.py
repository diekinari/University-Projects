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
# first_el = gen_rectangle(1, (3, 2.5, 0.5, 3.5), False)
# first_el = gen_re(1,angles=(60, 180, 120, 120), visualize=False)
first_el = gen_trapezoid(1, side_lengths=(4, 3, 3, 3), angles=(120, 120), visualize=False)
second_el = gen_trapezoid(1, side_lengths=(8, 6, 4, 6), angles=(120, 120), start_x=5, visualize=False)
visualize_polygons(map(lambda polygon: tr_rotate(polygon, 90),
                       tuple(gen_trapezoid(1, side_lengths=(4, 3, 3, 3), angles=(120, 120), visualize=False))))
