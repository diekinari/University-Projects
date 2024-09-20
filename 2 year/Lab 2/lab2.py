import tkinter as tk
import math

# Parameters for the layout
WINDOW_WIDTH = 800
GRAPH_HEIGHT = 300  # Adjust to give more space for the text below
PI_LINE_Y = GRAPH_HEIGHT // 2
PI = math.pi
SCALE_FACTOR = 150  # Increase for more pronounced oscillations
MAX_POINTS = 500  # Maximum number of points (set large for denser graph)


# Function to compute the next value of the Leibniz series
def leibniz_series_step(n):
    return 4 * (-1) ** n / (2 * n + 1)


class PiApproximationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab 2")
        self.root.configure(bg='black')

        # Create canvas for the top two-thirds
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=GRAPH_HEIGHT, bg='black')
        self.canvas.pack()

        self.pi_label = tk.Label(root, font=("Helvetica", 24), bg='white', fg='black')
        # заполнить всю оставшуюся часть экрана лейблом
        self.pi_label.pack(fill=tk.BOTH, expand=True)

        # Initialize approximation variables
        self.leibniz_approx = 0
        self.approximation_values = []
        self.step = 0

        # Draw the Pi reference line
        self.canvas.create_line(0, PI_LINE_Y, WINDOW_WIDTH, PI_LINE_Y, fill="white", width=2)

        # Start the animation
        self.animate()

    def animate(self):
        if self.step < 300:
            # Calculate next step in the Leibniz series
            self.leibniz_approx += leibniz_series_step(self.step)
            self.approximation_values.append(self.leibniz_approx)

            # Limit the number of points displayed and compress them
            if len(self.approximation_values) > MAX_POINTS:
                self.approximation_values.pop(0)

            # Update the number approximation display
            self.pi_label.config(text=f"{self.leibniz_approx:.10f}")

            # Clear previous lines
            self.canvas.delete("approximation")

            # Draw the continuous line for the oscillating values
            total_points = len(self.approximation_values)
            for i in range(total_points - 1):
                # Dynamically compress the x-values based on the number of points
                x1 = i * (WINDOW_WIDTH / total_points)  # Compress points dynamically to fit the window
                y1 = PI_LINE_Y - (self.approximation_values[i] - PI) * SCALE_FACTOR
                x2 = (i + 1) * (WINDOW_WIDTH / total_points)
                y2 = PI_LINE_Y - (self.approximation_values[i + 1] - PI) * SCALE_FACTOR

                # Draw a line connecting the points
                self.canvas.create_line(x1, y1, x2, y2, fill='white', tags="approximation")

            # Increment step and speed up rendering (20ms per frame)
            self.step += 1
            self.root.after(20, self.animate)  # Update every 20ms for faster rendering


root = tk.Tk()
app = PiApproximationApp(root)
root.mainloop()
