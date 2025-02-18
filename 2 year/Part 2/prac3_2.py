import pygame

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игрок и движение фона")

# Фон
background = pygame.image.load("background.jpeg")
bg_width = background.get_width()
bg_x = 0
bg_y = 0

# Спрайт игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("player.png")  # Загружаем изображение
        self.image = pygame.transform.scale(original_image, (50, 50))  # Уменьшаем размер
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        global bg_x, bg_y

        # Перемещение игрока
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Сдвиг фона, если игрок у края экрана
        if self.rect.right >= WIDTH:
            bg_x -= self.speed_x
            self.rect.right = WIDTH
        elif self.rect.left <= 0:
            bg_x -= self.speed_x
            self.rect.left = 0

        if self.rect.bottom >= HEIGHT:
            bg_y -= self.speed_y
            self.rect.bottom = HEIGHT
        elif self.rect.top <= 0:
            bg_y -= self.speed_y
            self.rect.top = 0

# Создание игрока
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    screen.blit(background, (bg_x, bg_y))  # Отображаем фон
    all_sprites.update()  # Обновляем спрайты
    all_sprites.draw(screen)  # Рисуем спрайты

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
            elif event.key == pygame.K_UP:
                player.speed_y = -5
            elif event.key == pygame.K_DOWN:
                player.speed_y = 5
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.speed_x = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player.speed_y = 0

    pygame.display.update()

pygame.quit()
