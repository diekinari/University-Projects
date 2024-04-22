import itertools
import random
from tkinter import Tk
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Polygon


# TODO
# switch user's funtction into system function(like rectangles are done) + implement 'random' task from chatGPT

def visualize_polygons(polygons_iterator):
    fig, ax = plt.subplots()
    ax.set_aspect('auto', 'datalim')

    for polygon in polygons_iterator:
        # print(polygon)
        poly_patch = Polygon(polygon, closed=True, edgecolor='black', linewidth=2, facecolor='none')
        # print(poly_patch)
        ax.add_patch(poly_patch)

    # ax.set_xticks([])
    # ax.set_yticks([])

    plt.xlim(-0.5, 10)
    plt.ylim(-3, 4)

    manager = plt.get_current_fig_manager()
    manager.set_window_title('Your Polygons')
    ax.set_axis_off()

    plt.show()


def _gen_rect(limit=50, vizualize=True):
    counter = itertools.islice(itertools.count(start=0, step=1), limit)
    polygons_list = []
    iterator = 0
    for x in counter:
        p = (x + iterator, 0)
        temp_l = []
        for y in range(4):
            if y == 0:
                temp_l.append(p)
            elif y == 1:
                temp_l.append((p[0], p[1] + 0.5))
            elif y == 2:
                temp_l.append((p[0] + 1, p[1] + 0.5))
            else:
                temp_l.append((p[0] + 1, p[1]))

        polygons_list.append(tuple(temp_l))
        iterator += 0.5

    if vizualize:
        visualize_polygons(polygons_list)
        return 'success'
    else:
        return polygons_list


def gen_rectangle(limit=50):
    return _gen_rect(limit)


def gen_triangle(limit=50, side_length=1, vizualize=True):
    counter = itertools.islice(itertools.count(start=0, step=1), limit)
    polygons_list = []
    iterator = 0
    for x in counter:
        x_coord = x + iterator
        y_coord = 0

        p1 = (x_coord, y_coord)
        # half of the botom side and height in equateral triangle(math 4 class)
        p2 = (x_coord + side_length / 2, y_coord + side_length * math.sqrt(3) / 2)
        p3 = (x_coord + side_length, y_coord)

        polygons_list.append((p1, p2, p3))

        iterator += side_length

    if vizualize:
        visualize_polygons(polygons_list)
    else:
        return polygons_list


def gen_hexagon(limit=50, side_length=1, vizualize=True):
    counter = itertools.islice(itertools.count(start=0, step=1), limit)
    polygons_list = []
    iterator = 0
    for x in counter:
        x_coord = (1.5 * side_length) * (x + iterator)
        y_coord = 0

        vertices = []
        for i in range(6):
            angle_rad = math.radians(60 * i)
            vertices.append((x_coord + side_length * math.cos(angle_rad), y_coord + side_length * math.sin(angle_rad)))

        polygons_list.append(tuple(vertices))

        iterator += side_length

    if vizualize:
        visualize_polygons(polygons_list)
    else:
        return polygons_list


def random_figures():
    total_figures = 7
    rectangles_limit = random.randint(1, total_figures - 2)  # случайное количество прямоугольников
    total_figures -= rectangles_limit
    triangles_limit = random.randint(1, total_figures - 1)  # случайное количество треугольников
    hexagons_limit = total_figures - triangles_limit  # оставшееся количество фигур - шестиугольники

    rectangles = gen_rectangle(limit=rectangles_limit, vizualize=False)
    triangles = gen_triangle(limit=triangles_limit, vizualize=False)
    hexagons = gen_hexagon(limit=hexagons_limit, vizualize=False)

    figures = [*rectangles, *triangles, *hexagons]
    random.shuffle(figures)
    # print(figures)
    visualize_polygons(figures)
