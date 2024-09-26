from tkinter import *
import math

windowWidth = 800
graphHeight = 300
piLineY = graphHeight // 2
pi = math.pi
scaleFactor = 150
maxPoints = 500


def leibniz_series_step(n):
    return 4 * (-1) ** n / (2 * n + 1)


class PiApproximation:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab 2")
        self.root.configure(bg='black')

        self.canvas = Canvas(root, width=windowWidth, height=graphHeight, bg='black')
        self.canvas.pack()

        self.pi_label = Label(root, font=("Helvetica", 24), bg='white', fg='black')
        self.pi_label.pack(fill=BOTH, expand=True)

        self.leibniz_approx = 0
        self.approximation_values = []
        self.step = 0

        self.canvas.create_line(0, piLineY, windowWidth, piLineY, fill="white", width=2)

        # Start the animation
        self.animate()

    def animate(self):
        if self.step < 300:
            self.leibniz_approx += leibniz_series_step(self.step)
            self.approximation_values.append(self.leibniz_approx)

            if len(self.approximation_values) > maxPoints:
                self.approximation_values.pop(0)

            self.pi_label.config(text=f"{self.leibniz_approx:.10f}")

            self.canvas.delete("approximation")

            total_points = len(self.approximation_values)
            for i in range(total_points - 1):
                x1 = i * (windowWidth / total_points)
                y1 = piLineY - (self.approximation_values[i] - pi) * scaleFactor
                x2 = (i + 1) * (windowWidth / total_points)
                y2 = piLineY - (self.approximation_values[i + 1] - pi) * scaleFactor

                self.canvas.create_line(x1, y1, x2, y2, fill='white', tags="approximation")

            self.step += 1
            self.root.after(20, self.animate)


root = Tk()
app = PiApproximation(root)
root.mainloop()
