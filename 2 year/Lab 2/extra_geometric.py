import tkinter as tk

# Constants
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 1000
GRAPH_HEIGHT = 800  # Height for the visualizations
GEOMETRIC_LINE_Y = GRAPH_HEIGHT * 3 // 4  # Middle of the graph for geometric series
SCALE_FACTOR = 1  # Scaling for the graph
MAX_POINTS = 500  # Maximum number of points to display


# Geometric Series step
def geometric_series_step(r, n):
    return r ** n


# Create the visualization app
class GeometricSeriesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Geometric Series Visualization")
        self.root.configure(bg='black')

        # Create canvas for the visualization
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=GRAPH_HEIGHT, bg='black')
        self.canvas.pack()

        # Label to display the current approximation value
        self.series_label = tk.Label(root, text="Geometric Series Term", font=("Helvetica", 24), bg='white', fg='black')
        self.series_label.pack(fill=tk.BOTH, expand=True)

        # Initialize variables
        self.r_value = 1.1  # The common ratio (adjustable)
        self.series_term = 1  # Start with the first term being 1 (r^0)
        self.series_values = []
        self.step = 0

        # Start the animation
        self.animate()

    def animate(self):
        if self.step < 100:  # Limit the number of steps
            # Calculate the next term in the geometric series
            current_term = geometric_series_step(self.r_value, self.step)
            self.series_values.append(current_term)

            # Limit the number of points displayed and compress them if necessary
            if len(self.series_values) > MAX_POINTS:
                self.series_values.pop(0)

            # Update the geometric series term display
            self.series_label.config(text=f"Geometric Term at n={self.step}: {current_term:.10f}")

            # Clear previous lines
            self.canvas.delete("approximation")

            # Draw the continuous line for the geometric series terms
            total_points = len(self.series_values)
            for i in range(total_points - 1):
                # Dynamically compress the x-values based on the number of points
                x1 = i * (WINDOW_WIDTH / total_points)
                y1 = GEOMETRIC_LINE_Y - self.series_values[i] * SCALE_FACTOR
                x2 = (i + 1) * (WINDOW_WIDTH / total_points)
                y2 = GEOMETRIC_LINE_Y - self.series_values[i + 1] * SCALE_FACTOR

                # Draw a line connecting the points
                self.canvas.create_line(x1, y1, x2, y2, fill='white', tags="approximation")

            # Increment step and continue animation
            self.step += 1
            self.root.after(100, self.animate)  # Slower animation (100 ms per frame)


# Create the Tkinter window and run the application
root = tk.Tk()
app = GeometricSeriesApp(root)
root.mainloop()
