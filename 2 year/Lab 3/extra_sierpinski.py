import tkinter as tk
import time

# Создание окна
window = tk.Tk()
window.title("Кривая Серпинского")
canvas_size = 600
canvas = tk.Canvas(window, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()

def draw_sierpinski_curve(points, order):
    if order == 0:
        # Если достигнут базовый случай, рисуем треугольник
        canvas.create_polygon(points, outline="black", fill="black")
        window.update()  # Обновление окна для анимации
        time.sleep(0.1)  # Небольшая задержка для видимой анимации
    else:
        # Вычисляем средние точки для построения нового уровня
        mid1 = ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2)
        mid2 = ((points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2)
        mid3 = ((points[2][0] + points[0][0]) / 2, (points[2][1] + points[0][1]) / 2)

        # Рекурсивные вызовы для трёх новых треугольников
        draw_sierpinski_curve([points[0], mid1, mid3], order - 1)  # Левый треугольник
        draw_sierpinski_curve([mid1, points[1], mid2], order - 1)  # Правый треугольник
        draw_sierpinski_curve([mid3, mid2, points[2]], order - 1)  # Нижний треугольник

# Начальные параметры для рисования кривой
initial_order = 5  # Начальный порядок (можно уменьшить для ускорения)
# Задаем начальные координаты треугольника
initial_points = [(canvas_size / 2, 0), (20, canvas_size), (canvas_size, canvas_size)]

# Рисуем кривую Серпинского
draw_sierpinski_curve(initial_points, initial_order)

window.mainloop()
