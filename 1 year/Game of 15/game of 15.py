# Головоломка представляет собой 15 квадратных костяшек с числами от 1 до 15.
# Все костяшки заключены в квадратную коробку (поле) размером 4 на 4.
# При размещении костяшек в коробке остается одно пустое место, которое можно использовать для перемещения костяшек внутри коробки.
# Цель игры - упорядочить размещение чисел в коробке, разместив их по возрастанию слева направо и сверху вниз,
# начиная с костяшки с номером 1 в левом верхнем углу и заканчивая пустым местом в правом нижнем углу коробки.
# Взаимодействие с программой производится через консоль.
# Игровое поле изображается в виде 4 текстовых строк и перерисовывается при каждом изменении состояния поля.
# При запросе данных от пользователя программа сообщает,
# что ожидает от пользователя (например, координаты очередного хода) и проверяет корректность ввода.
# Программа должна считать количество сделанных ходов, уметь автоматически определять недопустимые ходы, окончание партии и ее победителя.
# Сама программа НЕ ходит, т.е. не пытается упорядочить костяшки с целью выиграть игру.
import os
from time import *
from random import *


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, '_']
# ]


def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def isSolved(matrix):
    if (matrix[0] == [1, 2, 3, 4] and
            matrix[1] == [5, 6, 7, 8] and
            matrix[2] == [9, 10, 11, 12] and
            matrix[3] == [13, 14, 15, '_']):
        return True
    else:
        return False


def isSolvable(matrix):
    emptyBlockColumn = 0
    prevIsMoreThanCurrCount = 0
    previousElement = ''
    for string in range(4):
        for column in range(4):
            if matrix[string][column] == '_':
                emptyBlockColumn = column
                previousElement = ''
            elif string == column == 0 or previousElement == '':
                previousElement = matrix[string][column]
            else:
                if previousElement > matrix[string][column]:
                    prevIsMoreThanCurrCount += 1
                previousElement = matrix[string][column]
    if emptyBlockColumn + prevIsMoreThanCurrCount % 2 == 0:
        return True
    else:
        return False


def paint(matrix):
    clean()
    table = ['   1  2  3  4 ']
    for el in matrix:
        s = str(matrix.index(el) + 1) + '-' + '┃'
        for i in el:
            while len(s) % 3 != 0:
                s += ' '
            s += str(i) + ' '
        if len(str(el[3])) % 2 != 1:
            s = s.strip()
        s += '┃'
        table.append(s)
    for x in table:
        print(x)


def getAvailableCoordinates(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == '_':
                string = i
                column = j
                if string == 0:
                    if column == 0:
                        return [[string + 1, column], [string, column + 1]]
                    elif column == 1 or column == 2:
                        return [[string, column - 1], [string, column + 1], [string + 1, column]]
                    else:
                        return [[string, column - 1], [string + 1, column]]
                elif string == 1 or string == 2:
                    if column == 0:
                        return [[string + 1, column], [string, column + 1], [string - 1, column]]
                    elif column == 1 or column == 2:
                        return [[string, column - 1], [string, column + 1], [string - 1, column], [string + 1, column]]
                    else:
                        return [[string, column - 1], [string + 1, column], [string - 1, column]]
                elif string == 3:
                    if column == 0:
                        return [[string - 1, column], [string, column + 1]]
                    elif column == 1 or column == 2:
                        return [[string, column - 1], [string, column + 1], [string - 1, column]]
                    else:
                        return [[string, column - 1], [string - 1, column]]


def getEmptyCoordinates(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == '_':
                return [i, j]


def move(matrix):
    availableCoordinates = getAvailableCoordinates(matrix)
    while True:
        command = input('Для хода впишите номер строки и столбца через пробел (e.g. "3 4"): ')
        inputCoordinates = command.split(' ')

        if len(inputCoordinates) == 2 and inputCoordinates[0].isdigit() and inputCoordinates[1].isdigit() \
                and int(inputCoordinates[0]) <= 4 and int(inputCoordinates[1]) <= 4:
            inputCoordinates = [int(x) - 1 for x in command.split(' ')]
            if inputCoordinates in availableCoordinates:
                return inputCoordinates
            else:
                paint(matrix)
                print('Недопустимый ход! Попробуйте ещё раз')
        else:
            paint(matrix)
            print("Неккоректный ввод! Повторите попытку")


def play(box):
    # matrix = [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12],
    #     [13, 14, '_', 15]
    # ]
    matrix = box
    movesCounter = 0
    stepsStat = ''
    while not isSolved(matrix):
        paint(matrix)
        emptyCoordinates = getEmptyCoordinates(matrix)
        actionCoordinates = move(matrix)
        movesCounter += 1
        matrix[emptyCoordinates[0]][emptyCoordinates[1]] = matrix[actionCoordinates[0]][actionCoordinates[1]]
        matrix[actionCoordinates[0]][actionCoordinates[1]] = '_'
    if movesCounter % 10 == 1:
        stepsStat = 'Был сделан ' + str(movesCounter) + ' шаг'
    elif movesCounter % 10 == 2 or movesCounter % 10 == 3 or movesCounter % 10 == 4:
        stepsStat = 'Было сделано ' + str(movesCounter) + ' шага'
    else:
        stepsStat = 'Был сделано ' + str(movesCounter) + ' шагов'
    paint(matrix)
    print("✦•·····················•✦•·······················•✦")
    print("Головоломка решена! " + stepsStat)
    print('Перезапустите программу, чтобы решить её ещё раз ♡')
    print("✦•·····················•✦•·······················•✦")
    sleep(5)


def start():
    nums = list(range(1, 16))
    nums.append('_')
    shuffle(nums)
    matrix = [nums[i: i + 4] for i in range(0, len(nums), 4)]
    while not isSolvable(matrix):
        shuffle(nums)
        matrix = [nums[i: i + 4] for i in range(0, len(nums), 4)]
    play(matrix)


start()
