import pygame
import random

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Игрок, враги и стрела")

# Загрузка фона
background = pygame.image.load("background.jpeg")
bg_width, bg_height = background.get_size()
bg_x, bg_y = 0, 0

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        global bg_x, bg_y
        new_x = self.rect.x + self.speed_x
        new_y = self.rect.y + self.speed_y

        if 0 <= new_x <= WIDTH - self.rect.width:
            self.rect.x = new_x
        else:
            bg_x -= self.speed_x

        if 0 <= new_y <= HEIGHT - self.rect.height:
            self.rect.y = new_y
        else:
            bg_y -= self.speed_y

        bg_x = min(0, max(bg_x, WIDTH - bg_width))
        bg_y = min(0, max(bg_y, HEIGHT - bg_height))

# Класс врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, 2])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1

# Класс стрелы
class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_y = -7

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()  # Удаляем стрелу, если она вышла за экран

# Создание объектов
player = Player()
enemy1 = Enemy(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
enemy2 = Enemy(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy1, enemy2)

enemies = pygame.sprite.Group(enemy1, enemy2)
arrows = pygame.sprite.Group()

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (bg_x, bg_y))

    all_sprites.update()
    all_sprites.draw(screen)

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
            elif event.key == pygame.K_SPACE:  # Выстрел стрелой
                arrow = Arrow(player.rect.centerx, player.rect.top)
                all_sprites.add(arrow)
                arrows.add(arrow)
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.speed_x = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player.speed_y = 0

    # Проверка коллизий стрел и врагов
    for arrow in arrows:
        hit_enemies = pygame.sprite.spritecollide(arrow, enemies, True)
        if hit_enemies:
            arrow.kill()  # Удаляем стрелу, если попала во врага

    pygame.display.update()
    clock.tick(60)

pygame.quit()
