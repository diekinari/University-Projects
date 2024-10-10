import tkinter as tk
import math

window_width = 800
graph_height = 800
harmonic_line_y = graph_height // 2
scale_factor = 50
max_points = 500


def harmonic_series_step(n):
    return 1 / (n + 1)


class HarmonicSeriesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("lab 2 harmonic")
        self.root.configure(bg='black')

        self.canvas = tk.Canvas(root, width=window_width, height=graph_height, bg='black')
        self.canvas.pack()

        self.harmonic_label = tk.Label(root, text="Гармонический ряд", font=("Helvetica", 24), bg='white',
                                       fg='black')
        self.harmonic_label.pack(fill=tk.BOTH, expand=True)

        self.harmonic_approx = 0
        self.approximation_values = []
        self.step = 0

        self.canvas.create_line(0, harmonic_line_y, window_width, harmonic_line_y, fill="white", width=2)

        self.animate()

    def animate(self):
        if self.step < 10000:
            self.harmonic_approx += harmonic_series_step(self.step)
            self.approximation_values.append(self.harmonic_approx)

            if len(self.approximation_values) > max_points:
                self.approximation_values.pop(0)

            self.harmonic_label.config(text=f"Гармонический ряд: {self.harmonic_approx:.10f}")

            self.canvas.delete("approximation")

            total_points = len(self.approximation_values)
            for i in range(total_points - 1):
                x1 = i * (window_width / total_points)
                y1 = harmonic_line_y - self.approximation_values[i] * scale_factor
                x2 = (i + 1) * (window_width / total_points)
                y2 = harmonic_line_y - self.approximation_values[i + 1] * scale_factor

                self.canvas.create_line(x1, y1, x2, y2, fill='white', tags="approximation")

            self.step += 1
            self.root.after(100, self.animate)


root = tk.Tk()
app = HarmonicSeriesApp(root)
root.mainloop()
