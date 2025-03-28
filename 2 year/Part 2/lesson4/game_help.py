import pygame
from constants import *


class Help():
    def __init__(self):
        # Заголовок с крупным шрифтом
        self.title_font = pygame.font.Font(None, 48)
        # Текст команд – шрифт чуть меньше
        self.body_font = pygame.font.Font(None, 28)

        # Рендерим заголовок
        self.title_text = self.title_font.render("Управление:", True, C_WHITE)

        # Рендерим строки с командами, используя светло-голубой цвет
        self.command_texts = []
        self.command_texts.append(self.body_font.render("Влево: 'a' или стрелка влево", True, C_GREEN))
        self.command_texts.append(self.body_font.render("Вправо: 'd' или стрелка вправо", True, C_GREEN))
        self.command_texts.append(self.body_font.render("Прыжок: 'w' или стрелка вверх", True, C_GREEN))
        self.command_texts.append(self.body_font.render("Выстрел: пробел", True, C_GREEN))
        self.command_texts.append(
            self.body_font.render("Музыка вкл/выкл: 'm', громче: 'u', тише: 'j'", True, C_GREEN))
        self.command_texts.append(self.body_font.render("Подсказка (пауза): 'h'", True, C_GREEN))

        # Размеры подсказочного окна
        width = round(3 * win_width / 4)
        height = round(3 * win_height / 4)
        self.img = pygame.Surface((width, height), pygame.SRCALPHA)
        # Заполняем тёмным фоном с альфа-каналом (полупрозрачный)
        self.img.fill((30, 30, 30, 220))
        # Рисуем рамку вокруг окна
        pygame.draw.rect(self.img, C_WHITE, self.img.get_rect(), 4)

        # Отступы и позиционирование текста
        padding = 20
        y_offset = padding

        # Центрируем заголовок по горизонтали
        title_rect = self.title_text.get_rect(centerx=width // 2, top=y_offset)
        self.img.blit(self.title_text, title_rect)
        y_offset += title_rect.height + padding

        # Отрисовываем каждую команду с отступами слева
        for text in self.command_texts:
            text_rect = text.get_rect(left=padding, top=y_offset)
            self.img.blit(text, text_rect)
            y_offset += text_rect.height + 10

        # Создаем постоянную строку подсказок в нижней части экрана
        self.small_font = pygame.font.Font(None, 24)
        self.text_points = self.small_font.render("Очков:   ", True, C_WHITE)
        self.text_points_w = self.text_points.get_rect().width
        self.text_lives = self.small_font.render("Жизней:   ", True, C_WHITE)
        self.text_lives_w = self.text_lives.get_rect().width
        self.text_help = self.small_font.render("Пауза/подсказка: 'h'", True, C_WHITE)
        self.text_height = self.text_help.get_rect().height

    def line(self, points=0, lives=1):
        tab = 50
        # Создаем прозрачную поверхность для постоянной строки
        img = pygame.Surface((win_width, self.text_height), pygame.SRCALPHA)
        # Полупрозрачный фон для строки подсказок
        img.fill((0, 0, 0, 150))
        # Отрисовываем информацию о жизнях
        img.blit(self.text_lives, (10, 0))
        text = self.small_font.render(str(lives), True, C_YELLOW)
        img.blit(text, (10 + self.text_lives_w, 0))
        # Отрисовываем информацию об очках
        img.blit(self.text_points, (10 + self.text_lives_w + tab, 0))
        text = self.small_font.render(str(points), True, C_YELLOW)
        img.blit(text, (10 + self.text_lives_w + tab + self.text_points_w, 0))
        # Отрисовываем строку с подсказкой
        img.blit(self.text_help, (10 + self.text_lives_w + tab + self.text_points_w + tab, 0))
        return img
