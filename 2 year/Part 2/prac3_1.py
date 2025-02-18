import pygame

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Движение фона")

# Загрузка фона
bg = pygame.image.load("background.jpeg")  # Замените на ваш файл
bg_x, bg_y = 0, 0  # Начальные координаты фона
speed = 5  # Скорость движения

running = True
while running:
    screen.fill(WHITE)
    screen.blit(bg, (bg_x, bg_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # Движение фона вправо
        bg_x -= speed
    if keys[pygame.K_RIGHT]:  # Движение фона влево
        bg_x += speed
    if keys[pygame.K_UP]:  # Движение фона вниз
        bg_y -= speed
    if keys[pygame.K_DOWN]:  # Движение фона вверх
        bg_y += speed

    pygame.display.flip()

pygame.quit()
