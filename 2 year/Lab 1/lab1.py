from tkinter import *
import math

root = Tk()
c = Canvas(root, width=600, height=600, bg="gray")
c.pack()

ball = c.create_oval(100, 100, 500, 500, fill='lightblue')
dot = c.create_oval(100, 250, 110, 260, fill='red')

center_x, center_y = 300, 300
radius = 200
angle = 0


def motion():
    global angle
    speed = 0.01
    directionRight = True
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    c.coords(dot, x - 5, y - 5, x + 5, y + 5)

    if directionRight:
        angle += speed
    else:
        angle -= speed

    root.after(10, motion)


motion()
root.mainloop()
