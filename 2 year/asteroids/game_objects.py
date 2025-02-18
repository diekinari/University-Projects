import tkinter as tk
from math import sin, cos, radians
from random import randint
from config import *
from helpers import toroidal_wrap

class GameObject:
    def __init__(self, canvas, x, y, radius, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.id = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)

    def update_position(self, dx, dy, width, height):
        self.x += dx
        self.y += dy
        self.x, self.y = toroidal_wrap(self.x, self.y, width, height)
        self.canvas.coords(self.id, self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)

class Ship(GameObject):
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y, 15, "white")
        self.angle = 0
        self.thrust = 0

    def rotate(self, angle):
        self.angle += angle

    def accelerate(self):
        self.thrust = 1

    def decelerate(self):
        self.thrust = 0

    def move(self):
        dx = self.thrust * cos(radians(self.angle)) * 2
        dy = self.thrust * sin(radians(self.angle)) * 2
        return dx, dy

class Asteroid(GameObject):
    def __init__(self, canvas, x, y, radius):
        super().__init__(canvas, x, y, radius, "gray")
        # Случайная угловая и линейная скорость
        self.angle_speed = randint(-5, 5)
        self.linear_speed = randint(1, ASTEROID_SPEED)
        self.angle = randint(0, 360)

    def move(self):
        """Перемещение астероида с учетом его скорости и углового вращения."""
        dx = cos(radians(self.angle)) * self.linear_speed
        dy = sin(radians(self.angle)) * self.linear_speed
        self.x += dx
        self.y += dy
        self.angle += self.angle_speed
        return dx, dy

class Rocket(GameObject):
    def __init__(self, canvas, x, y, angle):
        super().__init__(canvas, x, y, 5, "red")
        self.angle = angle
        self.life_time = ROCKET_LIFETIME

    def move(self):
        """Перемещение ракеты в направлении ориентации корабля."""
        dx = cos(radians(self.angle)) * ROCKET_SPEED
        dy = sin(radians(self.angle)) * ROCKET_SPEED
        self.x += dx
        self.y += dy
        self.life_time -= 1  # Уменьшение времени жизни ракеты
        return dx, dy

    def is_alive(self):
        """Проверка, не истекло ли время жизни ракеты."""
        return self.life_time > 0
