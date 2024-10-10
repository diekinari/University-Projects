import tkinter as tk
import math

window_width = 700
window_height = 1000
graph_height = 800
geometric_line_y = graph_height * 3 // 4
scale_factor = 1
MAX_POINTS = 500


def geometric_series_step(r, n):
    return r ** n


class GeometricSeriesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("lab 3 extra geometric")
        self.root.configure(bg='black')

        self.canvas = tk.Canvas(root, width=window_width, height=graph_height, bg='black')
        self.canvas.pack()

        self.series_label = tk.Label(root, text="Геометрическая прогрессия: ", font=("Helvetica", 24), bg='white',
                                     fg='black')
        self.series_label.pack(fill=tk.BOTH, expand=True)

        self.r_value = 1.1
        self.series_term = 1
        self.series_values = []
        self.step = 0

        self.animate()

    def animate(self):
        if self.step < 100:
            current_term = geometric_series_step(self.r_value, self.step)
            self.series_values.append(current_term)

            if len(self.series_values) > MAX_POINTS:
                self.series_values.pop(0)

            self.series_label.config(text=f"Геометрическая прогрессия при n={self.step}: {current_term:.10f}")

            self.canvas.delete("approximation")

            total_points = len(self.series_values)
            for i in range(total_points - 1):
                x1 = i * (window_width / total_points)
                y1 = geometric_line_y - self.series_values[i] * scale_factor
                x2 = (i + 1) * (window_width / total_points)
                y2 = geometric_line_y - self.series_values[i + 1] * scale_factor

                self.canvas.create_line(x1, y1, x2, y2, fill='white', tags="approximation")

            self.step += 1
            self.root.after(100, self.animate)


root = tk.Tk()
app = GeometricSeriesApp(root)
root.mainloop()
