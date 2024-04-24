import itertools
import random
from tkinter import Tk
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Polygon


def visualize_polygons(polygons_iterator):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'datalim')

    for polygon in polygons_iterator:
        # print(polygon)
        poly_patch = Polygon(polygon, closed=True, edgecolor='black', linewidth=2, facecolor='none')
        # print(poly_patch)
        ax.add_patch(poly_patch)

    # ax.set_xticks([])
    # ax.set_yticks([])

    ax.annotate('', xy=(10, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='grey'))
    ax.annotate('', xy=(0, 10), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='grey'))

    xlim = (0, 10)

    plt.xlim(xlim)
    plt.ylim(xlim)

    manager = plt.get_current_fig_manager()
    manager.set_window_title('PolygonSuper')
    # ax.set_axis_off()

    plt.show()


# def gen_rectangle(limit=50, vizualize=True):
#     counter = itertools.islice(itertools.count(start=0, step=1), limit)
#     polygons_list = []
#     iterator = 0
#     for x in counter:
#         p = (x + iterator, 0)
#         temp_l = []
#         for y in range(4):
#             if y == 0:
#                 temp_l.append(p)
#             elif y == 1:
#                 temp_l.append((p[0], p[1] + 0.5))
#             elif y == 2:
#                 temp_l.append((p[0] + 1, p[1] + 0.5))
#             else:
#                 temp_l.append((p[0] + 1, p[1]))
#
#         polygons_list.append(tuple(temp_l))
#         iterator += 0.5
#
#     if vizualize:
#         visualize_polygons(polygons_list)
#         return 'success'
#     else:
#         return polygons_list


def gen_rectangle(limit=50, side_lengths=(1, 1, 1, 1), visualize=True):
    """
    Генерация последовательности четырехугольников.

    Аргументы:
    limit: Максимальное количество четырехугольников.
    side_lengths: Длины сторон четырехугольника. Представлены в виде кортежа (a, b, c, d),
                  где a - длина первой стороны, b - длина второй стороны, и так далее.
    visualize: Флаг для визуализации. Если True, будет отображена визуализация,
               иначе будет возвращен список координат.

    Возвращает:
    Если visualize равен True, отображает визуализацию четырехугольников.
    В противном случае возвращает список координат четырехугольников.
    """
    counter = itertools.islice(itertools.count(start=0, step=1), limit)
    polygons_list = []
    iterator = 0
    for x in counter:
        x_coord = x + iterator
        y_coord = 0

        p1 = (x_coord, y_coord)
        p2 = (x_coord + side_lengths[0], y_coord)
        p3 = (x_coord + side_lengths[0], y_coord + side_lengths[1])
        p4 = (x_coord, y_coord + side_lengths[2])
        polygons_list.append((p1, p2, p3, p4))

        iterator += max(side_lengths) + 0.5  # Добавляем небольшой отступ между четырехугольниками

    if visualize:
        visualize_polygons(polygons_list)
    else:
        return polygons_list


def gen_r(limit=50, side_lengths=(1, 1, 1, 1), angles=(90, 90, 90, 90), visualize=True):
    """
    Генерация последовательности четырехугольников.

    Аргументы:
    limit: Максимальное количество четырехугольников.
    side_lengths: Длины сторон четырехугольника. Представлены в виде кортежа (a, b, c, d), где
                  a - длина первой стороны, b - длина второй стороны, и так далее.
    angles: Углы четырехугольника в градусах. Представлены в виде кортежа (A, B, C, D), где
            A - угол между первой и второй стороной, B - угол между второй и третьей стороной, и так далее.
    visualize: Флаг для визуализации. Если True, будет отображена визуализация, иначе будет возвращен список координат.

    Возвращает:
    Если visualize равен True, отображает визуализацию четырехугольников. В противном случае возвращает список координат четырехугольников.
    """
    counter = itertools.islice(itertools.count(start=0, step=1), limit)
    polygons_list = []
    iterator = 0

    for x in counter:
        x_coord = x + iterator
        y_coord = 0

        p1 = (x_coord, y_coord)

        p2 = (p1[0] + math.cos(math.radians(angles[0])) * 1, p1[1] + math.sin(math.radians(angles[0])) * 1)
        p3 = (p2[0] + math.cos(math.radians(angles[1])) * 1, p2[1] + math.sin(math.radians(angles[1])) * 1)
        p4 = (p3[0] + math.cos(math.radians(angles[2])) * 1, p3[1] + math.sin(math.radians(angles[2])) * 1)

        polygons_list.append((p1, p2, p3, p4))
        iterator += max(side_lengths) + 0.5  # Добавляем небольшой отступ между четырехугольниками

    if visualize:
        visualize_polygons(polygons_list)
    else:
        return polygons_list


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


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def generate_random_figures():
    figures = []
    total_figures = 7
    base_x = 0  # Начальное значение X для первой фигуры
    distance_between_figures = 3  # Расстояние между фигурами в ряду

    while len(figures) < total_figures:
        figure_type = random.choice(["rectangle", "triangle", "hexagon"])

        if figure_type == "rectangle":
            figure = gen_rectangle(limit=1, vizualize=False)
        elif figure_type == "triangle":
            figure = gen_triangle(limit=1, vizualize=False)
        else:
            figure = gen_hexagon(limit=1, vizualize=False)

        tempFigure = []
        # adding minmum distance between figures
        for el in figure[0]:
            tempFigure.append((el[0] + base_x, el[1]))
        figure = [tuple(tempFigure)]

        # Добавляем фигуру в список
        figures.extend(figure)

        # Увеличиваем базовую X координату для следующей фигуры
        base_x += distance_between_figures

    visualize_polygons(figures)


def tr_translate(polygon, vector=(0, 5)):
    """
    Параллельный перенос (параллельный сдвиг) последовательности полигонов.

    Аргументы:
    polygon: Полигон, представленный в виде кортежа вершин.
    vector: Вектор сдвига, представленный в виде кортежа (dx, dy), где dx - смещение по оси X, а dy - смещение по оси Y.

    Возвращает:
    Новый полигон, в которой каждая вершина сдвинута на вектор сдвига.
    """
    translated_polygon = []
    for point in polygon:
        translated_point = (point[0] + vector[0], point[1] + vector[1])
        translated_polygon.append(translated_point)

    return tuple(translated_polygon)


def tr_rotate(polygon, angle=45):
    """
    Поворот полигона на заданный угол.

    Аргументы:
    polygon: Полигон, представленный в виде кортежа вершин.
    angle: Угол поворота в грудсах.

    Возвращает:
    Новый полигон, в котором каждая вершина повернута на заданный угол.
    """
    rotated_polygon = []
    for point in polygon:
        x = point[0]
        y = point[1]
        angle_radians = math.radians(angle)
        # Поворот вершины на заданный угол
        new_x = x * math.cos(angle_radians) - y * math.sin(angle_radians)
        new_y = x * math.sin(angle_radians) + y * math.cos(angle_radians)
        rotated_point = (new_x, new_y)
        rotated_polygon.append(rotated_point)

    return tuple(rotated_polygon)


def tr_symmetry(polygon, axis='x'):
    """
    Отражение полигона относительно выбранной оси.

    Аргументы:
    polygon: Полигон, представленный в виде кортежа вершин.
    axis: Ось симметрии. Может принимать значения 'x' или 'y'.

    Возвращает:
    Новый полигон, полученный после отражения исходного относительно выбранной оси.
    """
    symmetrical_polygon = []
    for point in polygon:
        x = point[0]
        y = point[1]
        # Отражение вершины относительно выбранной оси
        if axis == 'y':
            symmetrical_point = (-x, y)
        elif axis == 'x':
            symmetrical_point = (x, -y)
        else:
            raise ValueError("Неверное значение оси. Ось должна быть 'x' или 'y'.")
        symmetrical_polygon.append(symmetrical_point)

    return tuple(symmetrical_polygon)


def tr_homothety(polygon, scale_factor=5):
    """
    Гомотетия полигона относительно начала координат.

    Аргументы:
    polygon: Полигон, представленный в виде кортежа вершин.
    scale_factor: Коэффициент масштабирования.

    Возвращает:
    Новый полигон, полученный после гомотетии исходного относительно начала координат.
    """
    homothetic_polygon = []
    for point in polygon:
        x = point[0] * scale_factor
        y = point[1] * scale_factor
        homothetic_point = (x, y)
        homothetic_polygon.append(homothetic_point)

    return tuple(homothetic_polygon)
