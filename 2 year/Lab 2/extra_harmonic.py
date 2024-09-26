import tkinter as tk
import math

# Constants
WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 800
GRAPH_HEIGHT = 800  # Height for the visualizations
HARMONIC_LINE_Y = GRAPH_HEIGHT // 2  # Middle of the graph for Harmonic Series
SCALE_FACTOR = 50  # Scaling for the graph
MAX_POINTS = 500  # Maximum number of points to display
BATCH_SIZE = 10  # Calculate 10 steps per frame for faster convergence


# Harmonic Series step
def harmonic_series_step(n):
    return 1 / (n + 1)


# Create the visualization app
class HarmonicSeriesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Harmonic Series Visualization")
        self.root.configure(bg='black')

        # Create canvas for the visualization
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=GRAPH_HEIGHT, bg='black')
        self.canvas.pack()

        # Label to display the current approximation value
        self.harmonic_label = tk.Label(root, text="Harmonic Series Approximation", font=("Helvetica", 24), bg='white',
                                       fg='black')
        self.harmonic_label.pack(fill=tk.BOTH, expand=True)

        # Initialize approximation variables
        self.harmonic_approx = 0
        self.approximation_values = []
        self.step = 0

        # Draw the reference line for comparison (ln(n))
        self.canvas.create_line(0, HARMONIC_LINE_Y, WINDOW_WIDTH, HARMONIC_LINE_Y, fill="white", width=2)

        # Start the animation
        self.animate()

    def animate(self):
        if self.step < 10000:
            # Calculate the next step in the harmonic series
            self.harmonic_approx += harmonic_series_step(self.step)
            self.approximation_values.append(self.harmonic_approx)

            # Limit the number of points displayed and compress them if necessary
            if len(self.approximation_values) > MAX_POINTS:
                self.approximation_values.pop(0)

            # Update the harmonic series approximation display
            self.harmonic_label.config(text=f"Harmonic Approximation: {self.harmonic_approx:.10f}")

            # Clear previous lines
            self.canvas.delete("approximation")

            # Draw the continuous line for the harmonic series values
            total_points = len(self.approximation_values)
            for i in range(total_points - 1):
                # Dynamically compress the x-values based on the number of points
                x1 = i * (WINDOW_WIDTH / total_points)
                y1 = HARMONIC_LINE_Y - self.approximation_values[i] * SCALE_FACTOR
                x2 = (i + 1) * (WINDOW_WIDTH / total_points)
                y2 = HARMONIC_LINE_Y - self.approximation_values[i + 1] * SCALE_FACTOR

                # Draw a line connecting the points
                self.canvas.create_line(x1, y1, x2, y2, fill='white', tags="approximation")

            # Increment step and continue animation
            self.step += 1
            self.root.after(100, self.animate)  # Slower animation (100 ms per frame)


# Create the Tkinter window and run the application
root = tk.Tk()
app = HarmonicSeriesApp(root)
root.mainloop()
