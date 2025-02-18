import tkinter as tk
import math


class KochSnowflakeApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.level = 0  # Recursion depth
        self.width = 800
        self.height = 600

        # Initial inverted triangle points
        self.start_points = [
            (self.width // 2, self.height - 50),  # Bottom center
            (50, 100),  # Top left
            (self.width - 50, 100),  # Top right
        ]

        # Bind click to increase recursion depth
        self.root.bind("<Button-1>", self.handle_click)

        # Draw the initial snowflake
        self.draw_snowflake(self.start_points, self.level)

    def handle_click(self, event):
        """Handles click to increase recursion depth."""
        self.level += 1
        self.canvas.delete("all")

        # Recalculate points and normalize to fit the screen
        self.start_points = self.normalize_points(self.start_points, self.level)
        self.draw_snowflake(self.start_points, self.level)

    def draw_snowflake(self, points, level):
        """Draws the Koch snowflake for the current recursion level."""
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i + 1) % len(points)]
            self.draw_koch_line(p1, p2, level)

    def draw_koch_line(self, p1, p2, level):
        """Recursively draws Koch curve segments."""
        if level == 0:
            # Base case: draw a straight line
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="white", width=2)
        else:
            # Calculate intermediate points
            x1, y1 = p1
            x2, y2 = p2
            p3 = ((2 * x1 + x2) / 3, (2 * y1 + y2) / 3)  # First division point
            p4 = ((x1 + 2 * x2) / 3, (y1 + 2 * y2) / 3)  # Second division point

            # Peak of the equilateral triangle
            dx = x2 - x1
            dy = y2 - y1
            length = math.sqrt(dx**2 + dy**2) / 3
            angle = math.atan2(dy, dx) - math.pi / 3
            px = p3[0] + length * math.cos(angle)
            py = p3[1] + length * math.sin(angle)
            p5 = (px, py)

            # Recursive calls for the four new segments
            self.draw_koch_line(p1, p3, level - 1)
            self.draw_koch_line(p3, p5, level - 1)
            self.draw_koch_line(p5, p4, level - 1)
            self.draw_koch_line(p4, p2, level - 1)

    def normalize_points(self, points, level):
        """Normalizes the points to fit within the canvas."""
        # Expand the current points using Koch recursion
        expanded_points = []
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i + 1) % len(points)]
            expanded_points += self.recursively_expand(p1, p2, level)

        # Find bounding box of the expanded points
        min_x = min(p[0] for p in expanded_points)
        max_x = max(p[0] for p in expanded_points)
        min_y = min(p[1] for p in expanded_points)
        max_y = max(p[1] for p in expanded_points)

        # Scale to fit within the canvas
        scale_x = (self.width - 100) / (max_x - min_x)
        scale_y = (self.height - 100) / (max_y - min_y)
        scale = min(scale_x, scale_y)

        # Center the figure on the canvas
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        target_center_x = self.width / 2
        target_center_y = self.height / 2

        # Apply scaling and translation
        normalized_points = [
            (
                (p[0] - center_x) * scale + target_center_x,
                (p[1] - center_y) * scale + target_center_y,
            )
            for p in expanded_points
        ]

        return normalized_points

    def recursively_expand(self, p1, p2, level):
        """Recursively generates the points for the Koch curve."""
        if level == 0:
            return [p1, p2]
        else:
            # Calculate intermediate points
            x1, y1 = p1
            x2, y2 = p2
            p3 = ((2 * x1 + x2) / 3, (2 * y1 + y2) / 3)
            p4 = ((x1 + 2 * x2) / 3, (y1 + 2 * y2) / 3)
            dx = x2 - x1
            dy = y2 - y1
            length = math.sqrt(dx**2 + dy**2) / 3
            angle = math.atan2(dy, dx) - math.pi / 3
            px = p3[0] + length * math.cos(angle)
            py = p3[1] + length * math.sin(angle)
            p5 = (px, py)

            # Recursively expand each segment
            return (
                self.recursively_expand(p1, p3, level - 1)
                + self.recursively_expand(p3, p5, level - 1)[1:]
                + self.recursively_expand(p5, p4, level - 1)[1:]
                + self.recursively_expand(p4, p2, level - 1)[1:]
            )


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = KochSnowflakeApp(root)
    root.mainloop()
