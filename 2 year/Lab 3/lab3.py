import tkinter as tk
import time

width, height = 600, 600


def get_color(step, total_steps):
    r = 255
    g = int(255 * (step / total_steps))
    b = 0
    return f'#{r:02x}{g:02x}{b:02x}'


def hilbert_curve(order, x, y, xi, xj, yi, yj, canvas, prev_coords, draw_step, total_steps):
    if order <= 0:
        x_new = x + (xi + yi) // 2
        y_new = y + (xj + yj) // 2

        if prev_coords is not None:
            color = get_color(draw_step[0], total_steps)
            canvas.create_line(prev_coords[0], prev_coords[1], x_new, y_new, fill=color, width=2)

        if draw_step[0] % 1000 == 0:
            canvas.update()

        draw_step[0] += 1
        return x_new, y_new

    prev_coords = hilbert_curve(order - 1, x, y, yi // 2, yj // 2, xi // 2, xj // 2, canvas, prev_coords, draw_step,
                                total_steps)
    prev_coords = hilbert_curve(order - 1, x + xi // 2, y + xj // 2, xi // 2, xj // 2, yi // 2, yj // 2, canvas,
                                prev_coords, draw_step, total_steps)
    prev_coords = hilbert_curve(order - 1, x + xi // 2 + yi // 2, y + xj // 2 + yj // 2, xi // 2, xj // 2, yi // 2,
                                yj // 2, canvas, prev_coords, draw_step, total_steps)
    prev_coords = hilbert_curve(order - 1, x + xi // 2 + yi, y + xj // 2 + yj, -yi // 2, -yj // 2, -xi // 2, -xj // 2,
                                canvas, prev_coords, draw_step, total_steps)
    return prev_coords


def draw_hilbert(order, canvas):
    canvas.delete("all")
    draw_step = [0]
    total_steps = 4 ** order
    hilbert_curve(order, 0, 0, width, 0, 0, height, canvas, None, draw_step, total_steps)
    canvas.update()


root = tk.Tk()
root.title("Кривая Гильберта")
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()
order = 8
draw_hilbert(order, canvas)
root.mainloop()
