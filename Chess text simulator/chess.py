import os
from copy import deepcopy
from abc import ABC, abstractmethod
from icecream import ic

# Придумать 3 новых вида фигур с оригинальными правилами перемещения и реализовать их классы.
# сложность 1
#
# Реализовать возможность «отката» ходов. С помощью специальной команды можно возвращаться на ход
# (или заданное количество ходов) назад вплоть до начала партии.
# сложность 1
#
# Реализовать функцию подсказки выбора новой позиции фигуры: после выбора фигуры для хода функция визуально на поле
# показывает поля доступные для хода или фигуры соперника, доступные для взятия, выбранной фигурой.
# сложность 1
#
# Реализовать функцию подсказки угрожаемых фигур: она возвращает информацию о том, какие фигуры ходящего игрока сейчас
# находятся под боем (т.е. могут быть взяты соперником на следующий ход) и визуально выделяет их на поле.
# Функция отдельно указывает на наличие шаха королю.
# сложность 1
#
# Реализовать поддержку для пешки сложных правил: «взятие на проходе» и замены на другую фигуру при достижении крайней
# горизонтали
# сложность 1

COORDINATES = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
REV_COORDINATES = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}


class GoBackException(Exception): ...


class WrongStepException(Exception): ...


class Figure(ABC):
    def __init__(self, color):
        self.color = color
        self.dang = False
        self.sign = ""

    def __str__(self):
        begin = "\033[93m" if self.dang else ""
        end = "\033[0m" if self.dang else ""
        if self.color == "white":
            return begin + self.sign.upper() + end
        return begin + self.sign.lower() + end

    @abstractmethod
    def check_move(self, step):
        """implement your own check_move function"""


class Pawn(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.first_step = True
        self.sign = "p"
        self.dang = False

    def check_move(self, step, check=False):
        # координаты изначально переданной фигуры
        new_i, new_j = step.new
        if check:
            return Engine.check_pawn(step, check)
        else:
            if new_i in [0, 7]:
                return Engine.check_pawn(step, check) and Engine.make_choice(step)
            return Engine.check_pawn(step, check)


class Champion(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.sign = "c"
        self.dang = False

    def check_move(self, step):
        return Engine.check_champion(step) and (step.new_figure == "." or self.color != step.new_figure.color)


class Magician(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.sign = "m"
        self.dang = False

    def check_move(self, step):
        return Engine.check_magician(step) and (step.new_figure == "." or self.color != step.new_figure.color)


class Warrior(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.first_step = True
        self.sign = "w"
        self.dang = False

    def check_move(self, step, check=False):
        old_i, old_j = step.old
        new_i, new_j = step.new
        if self.first_step:
            cond = (old_i - new_i == 2 if step.figure.color == "white" else new_i - old_i == 2) and old_j == new_j
        else:
            cond = (old_i - new_i == 1 if step.figure.color == "white" else new_i - old_i == 1) and old_j == new_j
        self.first_step = False if check is False else self.first_step
        return (cond or Engine.check_warrior(step)) and (step.new_figure == "." or self.color != step.new_figure.color)


class Rook(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.sign = "r"
        self.dang = False

    def check_move(self, step):
        new_i, new_j = step.new
        return Engine.check_rook(step) and (step.board[new_i][new_j] == "." or self.color != step.new_figure.color)


class Knight(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.sign = "n"
        self.dang = False

    def check_move(self, step):
        new_i, new_j = step.new
        return Engine.check_knight(step) and (step.board[new_i][new_j] == "." or self.color != step.new_figure.color)


class Bishop(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.sign = "b"
        self.dang = False

    def check_move(self, step):
        new_i, new_j = step.new
        return Engine.check_bishop(step) and (step.board[new_i][new_j] == "." or self.color != step.new_figure.color)


class Queen(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.sign = "q"
        self.dang = False

    def check_move(self, step):
        new_i, new_j = step.new
        return (Engine.check_bishop(step) or Engine.check_rook(step)) and \
            (step.board[new_i][new_j] == "." or self.color != step.new_figure.color)


class King(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.sign = "k"
        self.dang = False

    def check_move(self, step):
        new_i, new_j = step.new
        return Engine.check_king(step) and (step.board[new_i][new_j] == "." or self.color != step.new_figure.color)


class Engine:
    @staticmethod
    def reform(c):
        i = 8 - int(c[1])
        j = COORDINATES[c[0]]
        return i, j

    @staticmethod
    def check_pawn(step, check):
        # координаты вражеской фигуры
        old_i, old_j = step.old
        # координаты изначальной фигуры
        new_i, new_j = step.new
        if step.new_figure == ".":  # Просто ход
            if old_j == new_j:  # Проверяем, чтобы он был вертикальным
                if step.figure.first_step:  # Если первый ход пешки
                    step.figure.first_step = check
                    if step.figure.color == "black":
                        step.figure.dang = new_i - old_i == 2 and Engine.en_passant(step)
                        return 1 <= new_i - old_i <= 2
                    else:
                        step.figure.dang = old_i - new_i == 2 and Engine.en_passant(
                            step)  # Проверка, это двойной ход или нет
                        return 1 <= old_i - new_i <= 2
                step.figure.dang = False  # Если уже не первый ход, то self.dang = False
                return new_i - old_i == 1 if step.figure.color == "black" else \
                    old_i - new_i == 1  # Либо на одну
            else:
                fig = step.board[old_i][new_j]
                if ((old_i - new_i == 1 if step.figure.color == "white" else old_i - new_i == 1) and
                        abs(new_j - old_j) == 1 and isinstance(fig, Pawn) and fig.dang):
                    if not check:
                        step.board[old_i][new_j] = "."
                        step.new = (new_i, new_j)
                    return True
        else:  # Если там стоит другая фигура
            if abs(new_j - old_j) == 1 and (old_i - new_i == 1 if step.figure.color == "white" else new_i - old_i == 1):
                return step.figure.color != step.new_figure.color
        if old_i in [1, 6]:
            step.figure.first_step = True
        return False

    # . . . * . . .
    # . . . * . . .
    # . . . * . . .
    # * * * R * * *
    # . . . * . . .
    # . . . * . . .
    # . . . * . . .
    @staticmethod
    def check_rook(step):
        old_i, old_j = step.old
        new_i, new_j = step.new
        if old_i == new_i:  # Если ход горизонтальный
            for j in range(min(old_j, new_j) + 1, max(old_j, new_j)):
                if step.board[new_i][j] != ".":
                    return False
        elif old_j == new_j:  # Или вертикальный
            for i in range(min(old_i, new_i) + 1, max(old_i, new_i)):
                if step.board[i][new_j] != ".":
                    return False
        else:
            return False
        return True

    # * . . . . . *
    # . * . . . * .
    # . . * . * . .
    # . . . B . . .
    # . . * . * . .
    # . * . . . * .
    # * . . . . . *
    @staticmethod
    def check_bishop(step):
        old_i, old_j = step.old
        new_i, new_j = step.new
        if abs(old_i - new_i) != abs(old_j - new_j):
            return False
        for i in range(min(old_i, new_i) + 1, max(old_i, new_i)):
            for j in range(min(old_j, new_j) + 1, max(old_j, new_j)):
                if abs(old_i - i) == abs(old_j - j):
                    if step.board[i][j] != "." and i != new_i and j != new_j:
                        return False
        return True

    # . . . . . . .
    # . * . * . * .
    # . . . * . . .
    # . * * C * * .
    # . . . * . . .
    # . * . * . * .
    # . . . . . . .

    @staticmethod
    def check_champion(step):
        old_i, old_j = step.old
        new_i, new_j = step.new
        if old_i == new_i:
            return abs(old_j - new_j) <= 2
        elif old_j == new_j:
            return abs(old_i - new_i) <= 2
        else:
            return abs(old_i - new_i) == 2 and abs(old_j - new_j) == 2

    # . . . . . . .
    # . . * . * . .
    # . * . . . * .
    # . . . N . . .
    # . * . . . * .
    # . . * . * . .
    # . . . . . . .
    @staticmethod
    def check_knight(step):
        old_i, old_j = step.old
        new_i, new_j = step.new
        return (abs(old_i - new_i) == 2 and abs(old_j - new_j) == 1) or \
            (abs(old_i - new_i) == 1 and abs(old_j - new_j) == 2)

    # . . * . * . .
    # . . . . . . .
    # * . * . * . *
    # . . . M . . .
    # * . * . * . *
    # . . . . . . .
    # . . * . * . .

    @staticmethod
    def check_magician(step):
        old_i, old_j = step.old
        new_i, new_j = step.new
        return (abs(old_i - new_i) == 1 and abs(old_j - new_j) == 1) or ((abs(old_i - new_i) == 3)
                                                                         and (abs(old_j - new_j) == 1)) or (
            (abs(old_i - new_i) == 1 and (abs(old_j - new_j) == 3)))

    # . . . . . . .
    # . . . . . . .
    # . . . . . . .
    # . . * * * . .
    # . * . W . * .
    # . . * * * . .
    # . . . . . . .

    @staticmethod
    def check_warrior(step):
        old_i, old_j = step.old
        new_i, new_j = step.new
        return ((old_i == new_i and abs(old_j - new_j) == 2) or
                (((step.figure.color == "white" and old_i - new_i == 1) or
                  (step.figure.color == "black" and new_i - old_i == 1)) and abs(old_j - new_j) == 1))

    # . . . . . . .
    # . . . . . . .
    # . . * * * . .
    # . . * K * . .
    # . . * * * . .
    # . . . . . . .
    # . . . . . . .

    @staticmethod
    def check_king(step):
        old_i, old_j = step.old
        new_i, new_j = step.new
        return abs(old_i - new_i) <= 1 and abs(old_j - new_j) <= 1

    @staticmethod
    def check_win(board):
        is_black_king_alive, is_white_king_alive = False, False
        for i in range(8):
            for j in range(8):
                if isinstance(board[i][j], King):
                    if board[i][j].color == "white":
                        is_white_king_alive = True
                    else:
                        is_black_king_alive = True
        if is_black_king_alive and is_white_king_alive:
            return False
        else:
            return "white" if not is_black_king_alive else "black"

    # . . . .
    # . * . .
    # . . . .
    # . p P .
    # . . . .
    @staticmethod
    def en_passant(step):
        new_i, new_j = step.new
        return (isinstance(step.board[new_i][new_j - 1] if new_j - 1 >= 0 else None, Pawn) or
                isinstance(step.board[new_i][new_j + 1] if new_j + 1 <= 7 else None,
                           Pawn))  # Проверка, это двойной ход или нет

    @staticmethod
    def is_dang(board_obj, coord, figure):
        board = board_obj.board
        for i in range(8):
            for j in range(8):
                # если объект фигура и она вражеская то проверяем её возможность хода относительно изначально переданной
                if board[i][j] != "." and board[i][j].color != figure.color:
                    if i != coord[0] and j != coord[1]:
                        # объект доски, координаты найденной вражеской, координаты переданной, объект переданной
                        # old - найденная вражеская фигура, new - изначально переданная фигура
                        step = Step(board_obj, (i, j), new=coord, new_figure=figure)
                        if step.is_available():
                            if isinstance(figure, King):
                                print("Шах!")
                            return True
        return False

    @staticmethod
    def make_choice(step):
        old_i, old_j = step.old
        data = {"ферзь": Queen(step.figure.color), "слон": Bishop(step.figure.color),
                "ладья": Rook(step.figure.color), "конь": Knight(step.figure.color),
                "маг": Magician(step.figure.color), "чемпион": Champion(step.figure.color)}
        inp = input("Введите желаемую фигуру (ферзь/слон/ладья/конь/маг/чемпион): ")
        while data.get(inp) is None:
            inp = input("Вы некорректно ввели название фигуры, попробуйте еще раз: ")
        step.board[old_i][old_j] = data[inp]
        step.figure = data[inp]
        return True


class Step:
    def __init__(self, board, old, new=None, new_figure=None):
        self.board_obj = board  # Объект доски
        self.board = self.board_obj.board  # Доска
        self.old = Engine.reform(old) if isinstance(old, str) else old  # Старые координаты
        self.new = new  # Новые координаты
        self.new_figure = new_figure  # Новая фигура по новым координатам
        self.figure = self.board[self.old[0]][self.old[1]]  # Старая Фигура

    def get_new(self, c):
        self.new = Engine.reform(c)
        self.new_figure = self.board[self.new[0]][self.new[1]]

    def is_available(self, check=True):
        return self.figure.check_move(self, check) if isinstance(self.figure, Pawn) \
            else self.figure.check_move(self)  # Если фигура может ходить

    def make_step(self, board):
        board[self.new[0]][self.new[1]] = self.figure
        board[self.old[0]][self.old[1]] = "."

    def get_hint_board(self):
        pseudo_board_obj = deepcopy(self.board_obj)
        for i in range(8):
            for j in range(8):
                temp_step = Step(pseudo_board_obj, self.old, (i, j), pseudo_board_obj.board[i][j])
                if temp_step.is_available():
                    # highlight empty cells
                    if pseudo_board_obj.board[i][j] == ".":
                        pseudo_board_obj.board[i][j] = "*"
                    else:
                        # highlight enemy cells
                        pseudo_board_obj.board[i][j] = "\033[31m" + str(pseudo_board_obj.board[i][j]) + "\033[0m"
        return pseudo_board_obj.show()


class Board:
    def __init__(self):
        self.board = []

    @staticmethod
    def clean():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def create_board(self):
        first_row = [
            [Pawn("black"), Warrior("black"), Pawn("black"),
             Pawn("black"), Pawn("black"), Pawn("black"),
             Warrior("black"), Pawn("black")],
            [Pawn("white"), Warrior("white"), Pawn("white"),
             Pawn("white"), Pawn("white"), Pawn("white"),
             Warrior("white"), Pawn("white")]
        ]
        other_black = [Champion("black"), Knight("black"), Bishop("black"), Queen("black"),
                       King("black"), Bishop("black"), Magician("black"), Rook("black")]
        other_white = [Champion("white"), Knight("white"), Bishop("white"), Queen("white"),
                       King("white"), Bishop("white"), Magician("white"), Rook("white")]
        self.board = [other_black,
                      first_row[0],
                      ["." for _ in range(8)],
                      ["." for _ in range(8)],
                      ["." for _ in range(8)],
                      ["." for _ in range(8)],
                      first_row[1],
                      other_white]

    def show(self, warning=False, color=None):
        Board.clean()
        cords = "    " + " ".join(list(map(lambda x: x.upper(), COORDINATES.keys()))) + "    "
        result = [cords, '\033[40m' + "      " + '\033[1m' + "BLACK SIDE" + "       " + '\033[0m']
        board_obj = deepcopy(self)
        board = board_obj.board
        if warning:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    piece = board[i][j]
                    if piece != ".":
                        # check white if current color is white, etc
                        if piece.color == color:
                            piece.dang = Engine.is_dang(board_obj, coord=(i, j), figure=piece)
                        else:
                            piece.dang = False
        for index, row in enumerate(board):
            result.append(
                f"{8 - index}" +
                '   ' +
                f"{' '.join(list(map(str, row)))}" +
                '   ' +
                f"{8 - index}"
            )

        result += ['\033[40m' + "\033[7m" + "      " + '\033[1m' + "WHITE SIDE" + "       " + '\033[0m', cords]

        return "\n".join(result)


class Game:
    def __init__(self):
        self.boards = []

    def add_to(self, board):
        self.boards.append(board)

    def back(self, n):
        for _ in range(n):
            self.boards.pop()


def main(board=None, current_step="white"):
    if board is None:
        board = Board()
        board.create_board()
    game = Game()
    game.add_to(board)
    while not isinstance(Engine.check_win(game.boards[-1].board), str):
        # вместе с отрисовкой показать предупреждения о фигурах стороны, которых могут съесть
        print(game.boards[-1].show(warning=True, color=current_step))
        try:
            piece_cords = input(
                f"Ход {len(game.boards)}, ходят {'белые' if current_step == 'white' else 'чёрные'}"
                f". Введите координаты фигуры, которой хотите походить: ")
            if piece_cords.startswith("назад"):
                n = int(piece_cords.split()[1])
                if len(game.boards) > n:
                    game.back(n)
                    current_step = "white" if len(game.boards) % 2 else "black"
                else:
                    raise GoBackException("Назад невозможно!")
            else:
                step = Step(game.boards[-1], piece_cords)
                if step.figure.color != current_step:
                    raise WrongStepException("Неправильный ход!")
                print(step.get_hint_board())
                new = input("Введите координаты, куда хотите пойти: ")
                step.get_new(new)
                if step.is_available(check=False):
                    board = deepcopy(game.boards[-1])
                    step.make_step(board.board)
                    game.add_to(board)
                    current_step = "black" if current_step == "white" else "white"
                else:
                    raise WrongStepException("Неправильный ход!")
        except Exception as e:
            print(e)
    else:
        print(f'Победили {"чёрные" if current_step == "white" else "белые"}. Игра закончена!')


main()
