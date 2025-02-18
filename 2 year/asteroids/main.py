import tkinter as tk
from random import randint

from game_objects import Ship, Asteroid, Rocket
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, INITIAL_LIVES, INITIAL_SCORE
from helpers import check_collision
from math import *


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Астероиды")
        self.canvas = tk.Canvas(self.root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg=BACKGROUND_COLOR)
        self.canvas.pack()

        # Начальные параметры
        self.score = INITIAL_SCORE
        self.lives = INITIAL_LIVES

        # Создание корабля
        self.ship = Ship(self.canvas, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Списки астероидов и ракет
        self.asteroids = []
        self.rockets = []

        self.running = False
        self.root.bind("<Left>", lambda _: self.ship.rotate(-10))
        self.root.bind("<Right>", lambda _: self.ship.rotate(10))
        self.root.bind("<Up>", lambda _: self.ship.accelerate())
        self.root.bind("<KeyRelease-Up>", lambda _: self.ship.decelerate())
        self.root.bind("<space>", lambda _: self.shoot())

    def shoot(self):
        """Выстрел ракеты из носа корабля."""
        x, y = self.ship.x + 15 * cos(radians(self.ship.angle)), self.ship.y + 15 * sin(radians(self.ship.angle))
        rocket = Rocket(self.canvas, x, y, self.ship.angle)
        self.rockets.append(rocket)

    def spawn_asteroid(self):
        """Создание нового астероида на экране."""
        x = randint(0, SCREEN_WIDTH)
        y = randint(0, SCREEN_HEIGHT)
        radius = randint(15, 40)
        asteroid = Asteroid(self.canvas, x, y, radius)
        self.asteroids.append(asteroid)

    def move_objects(self):
        """Перемещение всех объектов на экране."""
        for asteroid in self.asteroids:
            dx, dy = asteroid.move()
            asteroid.update_position(dx, dy, SCREEN_WIDTH, SCREEN_HEIGHT)

        for rocket in self.rockets:
            if rocket.is_alive():
                dx, dy = rocket.move()
                rocket.update_position(dx, dy, SCREEN_WIDTH, SCREEN_HEIGHT)
            else:
                self.canvas.delete(rocket.id)
                self.rockets.remove(rocket)

    def check_collisions(self):
        """Проверка столкновений ракеты с астероидом и корабля с астероидом."""
        for rocket in self.rockets:
            for asteroid in self.asteroids:
                if check_collision(rocket, asteroid):
                    self.canvas.delete(rocket.id)
                    self.canvas.delete(asteroid.id)
                    self.rockets.remove(rocket)
                    self.asteroids.remove(asteroid)
                    self.score += 1  # Увеличение счета за уничтожение астероида

        for asteroid in self.asteroids:
            if check_collision(self.ship, asteroid):
                self.canvas.delete(asteroid.id)
                self.asteroids.remove(asteroid)
                self.lives -= 1  # Уменьшение жизней при столкновении с астероидом
                if self.lives <= 0:
                    self.end_game()

    def end_game(self):
        """Конец игры, когда у игрока заканчиваются жизни."""
        self.running = False
        self.canvas.create_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, text="Game Over", fill="red", font=("Arial", 24))

    def game_loop(self):
        if self.running:
            self.move_objects()
            self.check_collisions()
            self.canvas.delete("score")
            self.canvas.create_text(10, 10, text=f"Score: {self.score}", fill="white", anchor=tk.NW, tags="score")
            self.canvas.delete("lives")
            self.canvas.create_text(SCREEN_WIDTH - 10, 10, text=f"Lives: {self.lives}", fill="white", anchor=tk.NE,
                                    tags="lives")

        self.root.after(16, self.game_loop)

    def start_game(self):
        """Начало игры, запуск генерации астероидов."""
        self.running = True
        self.game_loop()
        self.spawn_asteroid()  # Первая генерация астероида
        self.root.after(2000, self.spawn_asteroid)  # Генерация астероидов каждую 1-2 секунды

    def run(self):
        self.start_game()
        self.root.mainloop()


if __name__ == "__main__":
    Game().run()
