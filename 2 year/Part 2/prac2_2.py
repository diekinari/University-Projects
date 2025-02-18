import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы экрана
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ушаков Даниил Александроивч")

# Основной цикл первого упражнения
def draw_primitives():
    screen.fill(WHITE)

    # Закрашенный красный круг
    pygame.draw.circle(screen, RED, (200, 200), 50)

    # Круг в третьей четверти с контуром 15 пикселей
    pygame.draw.circle(screen, BLACK, (WIDTH // 4, HEIGHT * 3 // 4), 50, 15)

    # Круг в центре экрана
    pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), 100)

    # Прямоугольник 300x200
    pygame.draw.rect(screen, RED, (250, 250, 300, 200))

    # 5 случайных прямоугольников
    for _ in range(5):
        rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rand_rect = pygame.Rect(random.randint(0, WIDTH - 100), random.randint(0, HEIGHT - 100), random.randint(50, 200), random.randint(50, 200))
        pygame.draw.rect(screen, rand_color, rand_rect)

    # Домик из линий
    pygame.draw.polygon(screen, BLACK, [(400, 100), (300, 300), (500, 300)], 5)  # Крыша
    pygame.draw.rect(screen, BLACK, (330, 300, 140, 150), 5)  # Стены
    pygame.draw.rect(screen, BLACK, (370, 350, 50, 50), 5)  # Дверь

    # Произвольная фигура
    pygame.draw.polygon(screen, BLACK, [(50, 500), (100, 450), (150, 500), (200, 450), (250, 500)], 5)

    # Загрузка и перемещение изображения
    image = pygame.image.load("leaf.png")  # Подставьте свое изображение
    screen.blit(image, (300, 300))
    pygame.display.flip()

# Второе упражнение: анимация
def animate_shapes():
    clock = pygame.time.Clock()

    shapes = [
        {"shape": "square", "rect": pygame.Rect(100, 100, 50, 50), "color": (0, 255, 0), "dx": 5, "dy": 0},
        {"shape": "rectangle", "rect": pygame.Rect(200, 200, 80, 40), "color": (255, 0, 0), "dx": 3, "dy": 0},
        {"shape": "circle", "rect": pygame.Rect(300, 300, 50, 50), "color": (0, 0, 255), "dx": 4, "dy": 0},
        {"shape": "triangle", "rect": pygame.Rect(400, 400, 60, 60), "color": (255, 255, 0), "dx": 2, "dy": 0},
    ]

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for shape in shapes:
                    if shape["rect"].collidepoint(event.pos):
                        shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        for shape in shapes:
            shape["rect"].x += shape["dx"]

            # Отскок от стен
            if shape["rect"].right >= WIDTH or shape["rect"].left <= 0:
                shape["dx"] = -shape["dx"]
                shape["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            # Отрисовка фигур
            if shape["shape"] == "square":
                pygame.draw.rect(screen, shape["color"], shape["rect"])
            elif shape["shape"] == "rectangle":
                pygame.draw.rect(screen, shape["color"], shape["rect"])
            elif shape["shape"] == "circle":
                pygame.draw.circle(screen, shape["color"], shape["rect"].center, shape["rect"].width // 2)
            elif shape["shape"] == "triangle":
                pygame.draw.polygon(screen, shape["color"], [(shape["rect"].x, shape["rect"].y + 60),
                                                             (shape["rect"].x + 30, shape["rect"].y),
                                                             (shape["rect"].x + 60, shape["rect"].y + 60)])

        pygame.display.flip()
        clock.tick(60)

# Запуск упражнений
draw_primitives()
pygame.time.wait(2000)  # Пауза, чтобы увидеть результат первого задания
animate_shapes()

pygame.quit()
