from tkinter import *
from math import *

root = Tk()
c = Canvas(root, width=600, height=600, bg="gray")
c.pack()

ball = c.create_oval(100, 100, 500, 500, fill='lightblue')
dot = c.create_oval(100, 250, 110, 260, fill='pink')

centralX, centralY = 300, 300
radius = 200
angle = 0
speed = 0.01
directionRight = True


def change_direction():
    global directionRight
    directionRight = not directionRight


def increase_speed():
    global speed
    speed += 0.09


def decrease_speed():
    global speed
    if speed - 0.09 < 0:
        if speed - 0.01 >= 0:
            speed -= 0.01
            return
        else:
            return
    speed -= 0.09


def motion():
    global angle
    # directionRight = True
    x = centralX + radius * cos(angle)
    y = centralY + radius * sin(angle)
    c.coords(dot, x - 5, y - 5, x + 5, y + 5)
    if directionRight:
        angle += speed
    else:
        angle -= speed
    # print(speed)
    root.after(10, motion)


directionButton = Button(text="Direction", command=change_direction)
increaseButton = Button(text="Increase Speed", command=increase_speed)
decreaseButton = Button(text="Decrease Speed", command=decrease_speed)
directionButton.pack()
increaseButton.pack()
decreaseButton.pack()
motion()
root.mainloop()
