import itertools
import functools
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


def gen_trapezoid(limit=50, side_lengths=(1, 1, 1, 1), angles=(90, 90), start_x=0, visualize=True):
    """
    Генерация последовательности трапеций.

    Аргументы:
    limit: Максимальное количество трапеций.
    side_lengths: Длины сторон трапеции. Представлены в виде кортежа (a, b, c, d),
                  где a - длина нижнего основания, b - длина левой стороны, c - длина верхнего основания, d - длина правой стороны.
    angles: Углы при нижнем основании трапеции в градусах. Представлены в виде кортежа (A, B),
            где A - угол при левом нижнем углу, B - угол при правом нижнем углу.
    start_x: Начальная координата по оси X для генерации трапеций.
    visualize: Флаг для визуализации. Если True, будет отображена визуализация,
               иначе будет возвращен список координат.

    Возвращает:
    Если visualize равен True, отображает визуализацию трапеций.
    В противном случае возвращает список координат трапеций.
    """
    counter = itertools.islice(itertools.count(start=start_x, step=1), limit)
    trapezoids_list = []
    iterator = start_x
    for _ in counter:
        x_coord = iterator
        y_coord = 0

        p1 = (x_coord, y_coord)
        p2 = (x_coord + side_lengths[0], y_coord)

        # Расчет координат для верхнего левого угла трапеции
        delta_x_b = math.cos(math.radians(180 - angles[0])) * side_lengths[1]
        delta_y_b = math.sin(math.radians(180 - angles[0])) * side_lengths[1]
        p3 = (p1[0] + delta_x_b, p1[1] + delta_y_b)

        # Расчет координат для верхнего правого угла трапеции
        delta_x_d = math.cos(math.radians(angles[1])) * side_lengths[3]
        delta_y_d = math.sin(math.radians(angles[1])) * side_lengths[3]
        p4 = (p2[0] + delta_x_d, p2[1] + delta_y_d)

        trapezoids_list.append((p1, p2, p4, p3))

        # Расчет следующей стартовой позиции
        iterator += side_lengths[0] + max(delta_x_b, delta_x_d) + 0.5  # Добавляем небольшой отступ между трапециями

    if visualize:
        visualize_polygons(trapezoids_list)
    else:
        return trapezoids_list


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
    Поворот полигона на заданный угол

    Аргументы:
    polygon: Полигон, представленный в виде кортежа вершин
    angle: Угол поворота в грудсах

    Возвращает:
    Новый полигон, в котором каждая вершина повернута на заданный угол
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
    Отражение полигона относительно выбранной оси

    Аргументы:
    polygon: Полигон, представленный в виде кортежа вершин
    axis: Ось симметрии. Может принимать значения 'x' или 'y'

    Возвращает:
    Новый полигон, полученный после отражения исходного относительно выбранной оси
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
    Гомотетия полигона относительно начала координат

    Аргументы:
    polygon: Полигон, представленный в виде кортежа вершин
    scale_factor: Коэффициент масштабирования

    Возвращает:
    Новый полигон, полученный после гомотетии исходного относительно начала координат
    """
    homothetic_polygon = []
    for point in polygon:
        x = point[0] * scale_factor
        y = point[1] * scale_factor
        homothetic_point = (x, y)
        homothetic_polygon.append(homothetic_point)

    return tuple(homothetic_polygon)


def flt_convex_polygon(polygon):
    """
    Проверяет, является ли многоугольник выпуклым

    Аргументы:
    polygon: Многоугольник, представленный в виде списка вершин

    Возвращает:
    True, если многоугольник выпуклый, иначе False
    """
    if len(polygon) < 3:
        return False

    def cross_product_orientation(point1, point2, point3):
        """
        Возвращает положительное значение, если точки образуют левый поворот,
        отрицательное для правого поворота, и 0, если точки коллинеарны

        Это происходит из-за того, что результат – это площадь паралеллограма, образованного двумя линиями(P1P2 и P1P3)
        Из определения векторного произведения:
        1) Если определитель положителен, то тройка векторов имеет ту же ориентацию, что и система координат
        2) Если отрицателен, то тройка векторов имеет ориентацию, противоположную ориентации системы координат
        3) Если определитель равен нулю, то векторы компланарны (линейно зависимы)

        В нашем случае пространство – двумерное, и, следовательно, система координат имеет заданную ориентацию
        Точки:
        P1 = (Ax, Ay), P2 = (Bx, By), P3 = (Cx, Cy)
        Формула:
        ((Bx - Ax) * (Cy - Ay)) - ((By - Ay) * (Cx - Ax))
        """
        return ((point2[0] - point1[0]) * (point3[1] - point1[1])) - ((point2[1] - point1[1]) * (point3[0] - point1[0]))

    # Знак первого векторного произведения
    sign = None
    for i in range(len(polygon)):
        # Зацикливающиеся в рамках длины полигона индексы
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        p3 = polygon[(i + 2) % len(polygon)]
        cp = cross_product_orientation(p1, p2, p3)

        if cp != 0:
            if sign is None:
                # Если первым вектором не выяснялся знак, то определяем его
                sign = cp > 0
            # Знак не совпадает с знаком первого вектора – многоугольник не выпуклый т.к. был поворот в друную сторону
            elif (cp > 0) != sign:
                return False

    return True


def flt_angle_point(point, polygon):
    """
    Проверяет, содержит ли многоугольник заданную точку

    Аргументы:
    point: Точка, в виде кортежа координат
    polygon: Многоугольник, в виде списка вершин

    Возвращает:
    True, если многоугольник содержит точку, или False если нет
    """
    return point in polygon


def flt_square(area, polygon):
    """
        Проверяет, является ли площадь многоугольника меньше заданной площади

        Аргументы:
        square: Площадь
        polygon: Многоугольник, в виде списка вершин

        Возвращает:
        True, если площадь многоугольника меньше, или False если нет
        """

    def calculate_polygon_area(actual_polygon):
        # По теореме площади Гаусса
        num_points = len(actual_polygon)
        actual_area = 0.0
        for i in range(num_points):
            j = (i + 1) % num_points  # Индекс следующей вершины
            actual_area += actual_polygon[i][0] * actual_polygon[j][1]
            actual_area -= actual_polygon[j][0] * actual_polygon[i][1]
        actual_area = abs(actual_area) / 2
        return actual_area

    return calculate_polygon_area(polygon) < area


def flt_shortest_side(side_length, polygon):
    """
    Проверяет, меньше ли кратчайшая сторона многоугольника заданного значения

    Аргументы:
    polygon: Многоугольник, в виде списка вершин
    side_length: Заданное значение стороны для сравнения

    Возвращает:
    True, если кратчайшая сторона меньше заданного значения, или False если нет
    """

    def calculate_distance(p1, p2):
        # По теореме Пифагора
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    num_points = len(polygon)
    shortest_side = math.inf  # Cамая большая возможная величина стороны

    for i in range(num_points):
        j = (i + 1) % num_points
        side = calculate_distance(polygon[i], polygon[j])
        if side < shortest_side:
            shortest_side = side

    return shortest_side < side_length


def flt_point_inside(point, polygon):
    def point_in_polygon():
        """
        Проверяет, содержится ли точка в многоугольнике через метод трассировки луча

        Аргументы:
        point: Точка, в виде кортежа координат
        polygon: Многоугольник, в виде списка вершин

        Возвращает:
        True, если точка находится внутри многоугольника, иначе False
        """
        intersections_count = 0
        for i in range(len(polygon)):
            j = (i + 1) % len(polygon)
            # Находится ли точка между вершинами по вертикали
            # И правее ли находится другая точка на ребре с той-же y-координатой (формула линейной интерполяции)
            if ((polygon[i][1] > point[1]) != (polygon[j][1] > point[1])) and \
                    (point[0] < (polygon[j][0] - polygon[i][0]) * (point[1] - polygon[i][1]) / (
                            polygon[j][1] - polygon[i][1]) + polygon[i][0]):
                intersections_count += 1
        return intersections_count % 2 == 1

    return flt_convex_polygon(polygon) and point_in_polygon()


def calculate_angle(p1, p2, p3):
    """
    Вычисляет угол между тремя точками, где p2 это вершина угла

    Аргументы:
    p1, p2, p3: Точки в виде кортежей координат (x, y)

    Возвращает:
    Угол в радианах
    """
    # Вычисляем расстояние между вершинами по теореме Пифагора
    a = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    b = math.sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
    c = math.sqrt((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2)
    # Переворачиваем теорему косинусов(a^2 + b^2 - 2*a*b*cos(x)) и находим arccos угла
    angle = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    return angle


def get_polygon_angles(polygon):
    """
    Вычисляет углы многоугольника.

    Аргументы:
    polygon: Многоугольник, в виде списка вершин.

    Возвращает:
    Список углов в радианах.
    """
    angles = []
    n = len(polygon)
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]
        p3 = polygon[(i + 2) % n]
        angle = calculate_angle(p1, p2, p3)
        angles.append(angle)
    return angles


def flt_polygon_angles_inside(polygon1, polygon2):
    """
    Проверяет, является ли второй многоугольник выпуклым и имеет ли общий угол с первым многоугольником

    Аргументы:
    polygon1: Первый многоугольни
    polygon2: Второй многоугольник

    Возвращает:
    True, если второй многоугольник выпуклый и имеет хотя бы один общий угол с первым многоугольником, или False
    """
    if not flt_convex_polygon(polygon2):
        return False

    angles1 = get_polygon_angles(polygon1)
    angles2 = get_polygon_angles(polygon2)

    for angle1 in angles1:
        for angle2 in angles2:
            if math.isclose(angle1, angle2, rel_tol=1e-5):
                return True

    return False
