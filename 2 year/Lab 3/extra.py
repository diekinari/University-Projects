import tkinter as tk
import time
import math

window = tk.Tk()
window.title("Кривая Коха")
canvas_size = 600
canvas = tk.Canvas(window, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()

def draw_line(x1, y1, x2, y2, color="black"):
    canvas.create_line(x1, y1, x2, y2, fill=color)
    window.update()

def koch_curve(x1, y1, x2, y2, depth):
    if depth == 0:
        draw_line(x1, y1, x2, y2)
    else:
        # точка для деления отрезка на три части
        dx = (x2 - x1) / 3
        dy = (y2 - y1) / 3

        # точка для деления отрезка
        xA = x1 + dx
        yA = y1 + dy

        xB = x1 + 2 * dx
        yB = y1 + 2 * dy

        # точка для "вершины" треугольника
        x_mid = (xA + xB) / 2
        y_mid = (yA + yB) / 2

        # вершина треугольника(поворот на 60 градусов)
        angle = math.radians(60)
        xC = x_mid + (xB - xA) * math.cos(angle) - (yB - yA) * math.sin(angle)
        yC = y_mid + (xB - xA) * math.sin(angle) + (yB - yA) * math.cos(angle)

        koch_curve(x1, y1, xA, yA, depth - 1)
        koch_curve(xA, yA, xC, yC, depth - 1)
        koch_curve(xC, yC, xB, yB, depth - 1)
        koch_curve(xB, yB, x2, y2, depth - 1)

initial_depth = 4
x_start = 50
y_start = 50
x_end = 550
y_end = 50


koch_curve(x_start, y_start, x_end, y_end, initial_depth)

window.mainloop()
