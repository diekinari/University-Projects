import math

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk  # Python 2

DELAY = 100
CIRCULAR_PATH_INCR = 10

sin = lambda degs: math.sin(math.radians(degs))
cos = lambda degs: math.cos(math.radians(degs))


class Celestial(object):
    # Constants
    COS_0, COS_180 = cos(0), cos(180)
    SIN_90, SIN_270 = sin(90), sin(270)

    def __init__(self, x, y, radius):
        self.x, self.y = x, y
        self.radius = radius

    def bounds(self):
        """ Return coords of rectangle surrounding circlular object. """
        return (self.x + self.radius * self.COS_0, self.y + self.radius * self.SIN_270,
                self.x + self.radius * self.COS_180, self.y + self.radius * self.SIN_90)


def circular_path(x, y, radius, delta_ang, start_ang=0):
    """ Endlessly generate coords of a circular path every delta angle degrees. """
    ang = start_ang % 360
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360


def update_position(canvas, id, celestial_obj, path_iter):
    celestial_obj.x, celestial_obj.y = next(path_iter)  # iterate path and set new position
    # update the position of the corresponding canvas obj
    x0, y0, x1, y1 = canvas.coords(id)  # coordinates of canvas oval object
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # current center point
    dx, dy = celestial_obj.x - oldx, celestial_obj.y - oldy  # amount of movement
    canvas.move(id, dx, dy)  # move canvas oval object that much
    # repeat after delay
    canvas.after(DELAY, update_position, canvas, id, celestial_obj, path_iter)


top = tk.Tk()
top.title('Circular Path')

canvas = tk.Canvas(top, bg='white', height=500, width=500)
canvas.pack()

sol_obj = Celestial(250, 250, 25)
planet_obj1 = Celestial(250 + 100, 250, 15)
sol = canvas.create_oval(sol_obj.bounds(), fill='yellow', width=0)
planet1 = canvas.create_oval(planet_obj1.bounds(), fill='blue', width=0)

orbital_radius = math.hypot(sol_obj.x - planet_obj1.x, sol_obj.y - planet_obj1.y)
path_iter = circular_path(sol_obj.x, sol_obj.y, orbital_radius, CIRCULAR_PATH_INCR)
next(path_iter)  # prime generator

top.after(DELAY, update_position, canvas, planet1, planet_obj1, path_iter)
top.mainloop()
