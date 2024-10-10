import tkinter as tk
import time

# Размеры экрана и шаг
width, height = 600, 600

# Функция для расчета цвета, плавно переходящего от красного к зелёному
def get_color(step, total_steps):
    r = 255  # Уменьшаем красный компонент
    g = int(255 * (step / total_steps))  # Увеличиваем зелёный компонент
    b = 0
    return f'#{r:02x}{g:02x}{b:02x}'  # Преобразуем RGB в hex-формат для Tkinter


# Рекурсивная функция для рисования кривой Гильберта
def hilbert_curve(order, x, y, xi, xj, yi, yj, canvas, prev_coords, draw_step, total_steps):
    if order <= 0:
        # Новая точка
        x_new = x + (xi + yi) // 2
        y_new = y + (xj + yj) // 2

        # Если есть предыдущие координаты, рисуем линию с изменяющимся цветом
        if prev_coords is not None:
            color = get_color(draw_step[0], total_steps)  # Получаем цвет для текущего шага
            canvas.create_line(prev_coords[0], prev_coords[1], x_new, y_new, fill=color, width=2)

        # Обновляем экран каждые 100 шагов для ускорения
        if draw_step[0] % 100 == 0:
            canvas.update()

        # Увеличиваем счётчик шагов
        draw_step[0] += 1

        # Возвращаем новые координаты
        return x_new, y_new

    # Рекурсивные вызовы для каждого сегмента кривой
    prev_coords = hilbert_curve(order - 1, x, y, yi // 2, yj // 2, xi // 2, xj // 2, canvas, prev_coords, draw_step,
                                total_steps)
    prev_coords = hilbert_curve(order - 1, x + xi // 2, y + xj // 2, xi // 2, xj // 2, yi // 2, yj // 2, canvas,
                                prev_coords, draw_step, total_steps)
    prev_coords = hilbert_curve(order - 1, x + xi // 2 + yi // 2, y + xj // 2 + yj // 2, xi // 2, xj // 2, yi // 2,
                                yj // 2, canvas, prev_coords, draw_step, total_steps)
    prev_coords = hilbert_curve(order - 1, x + xi // 2 + yi, y + xj // 2 + yj, -yi // 2, -yj // 2, -xi // 2, -xj // 2,
                                canvas, prev_coords, draw_step, total_steps)

    return prev_coords


# Функция запуска анимации
def draw_hilbert(order, canvas):
    canvas.delete("all")  # Очистка экрана перед каждым запуском
    draw_step = [0]  # Счётчик шагов для контроля обновлений
    total_steps = 4 ** order  # Всего шагов для кривой порядка n
    hilbert_curve(order, 0, 0, width, 0, 0, height, canvas, None, draw_step, total_steps)
    canvas.update()  # Последнее обновление экрана после завершения


# Создание окна Tkinter
root = tk.Tk()
root.title("Кривая Гильберта с плавным градиентом")

# Создание холста для рисования
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

# Начальное значение порядка
order = 7  # Высокий порядок для демонстрации

# Запуск отрисовки
draw_hilbert(order, canvas)

# Запуск основного цикла Tkinter
root.mainloop()
