import itertools
from tkinter import Tk
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def visualize_polygons(polygons_iterator):
    fig, ax = plt.subplots()
    ax.set_aspect('auto', 'datalim')

    for polygon in polygons_iterator:
        poly_patch = Polygon(polygon, closed=True, edgecolor='black', linewidth=2, facecolor='none')
        ax.add_patch(poly_patch)

    # ax.set_xticks([])
    # ax.set_yticks([])

    plt.xlim(-0.5, 10)
    plt.ylim(-3, 4)
    ax.autoscale_view()

    manager = plt.get_current_fig_manager()
    manager.set_window_title('Your Polygons')

    plt.show()


def gen_rectangle(limit=50):
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

    visualize_polygons(polygons_list)
