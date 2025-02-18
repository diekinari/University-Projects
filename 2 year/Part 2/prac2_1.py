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
pygame.display.set_caption("Ушаков Даниил Александроивч")  # Укажите свое ФИО

# Загрузка изображения
image = pygame.image.load("leaf.png")  # Подставьте путь к изображению
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Создание 5 случайных прямоугольников один раз
random_rects = []
for _ in range(5):
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    rand_rect = pygame.Rect(random.randint(0, WIDTH - 100), random.randint(0, HEIGHT - 100),
                            random.randint(50, 200), random.randint(50, 200))
    random_rects.append((rand_rect, rand_color))


# Функция отрисовки объектов
def draw_scene():
    screen.fill(WHITE)

    # Закрашенный красный круг
    pygame.draw.circle(screen, RED, (200, 200), 50)

    # Круг в третьей четверти с контуром 15 пикселей
    pygame.draw.circle(screen, BLACK, (WIDTH // 4, HEIGHT * 3 // 4), 50, 15)

    # Круг в центре экрана
    pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), 100)

    # Прямоугольник 300x200
    pygame.draw.rect(screen, RED, (250, 250, 300, 200))

    # Рисование заранее созданных случайных прямоугольников
    for rect, color in random_rects:
        pygame.draw.rect(screen, color, rect)

    # Домик (крыша по центру экрана)
    roof_top = (WIDTH // 2, HEIGHT // 4)  # Верхушка крыши
    house_base = [
        (WIDTH // 2 - 100, HEIGHT // 4 + 100),  # Левый нижний угол
        (WIDTH // 2 + 100, HEIGHT // 4 + 100),  # Правый нижний угол
    ]
    pygame.draw.polygon(screen, BLACK, [roof_top] + house_base, 5)  # Крыша
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 90, HEIGHT // 4 + 100, 180, 150), 5)  # Стены
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 25, HEIGHT // 4 + 150, 50, 50), 5)  # Дверь

    # Произвольная фигура
    pygame.draw.polygon(screen, BLACK, [(50, 500), (100, 450), (150, 500), (200, 450), (250, 500)], 5)

    # Вывод изображения
    screen.blit(image, image_rect)


# Основной цикл программы
running = True
moving = False  # Флаг перемещения изображения
offset_x, offset_y = 0, 0  # Смещение курсора внутри изображения

while running:
    screen.fill(WHITE)
    draw_scene()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if image_rect.collidepoint(event.pos):
                moving = True
                offset_x = event.pos[0] - image_rect.x
                offset_y = event.pos[1] - image_rect.y

        elif event.type == pygame.MOUSEBUTTONUP:
            moving = False

        elif event.type == pygame.MOUSEMOTION and moving:
            image_rect.x = event.pos[0] - offset_x
            image_rect.y = event.pos[1] - offset_y

    pygame.display.flip()

pygame.quit()
