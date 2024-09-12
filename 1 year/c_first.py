import os


# TODO
# 1) Develop proper getting available positions thoughout every point (tech, spec & filter). Castling required.
# 2) Next, implement highlighting available positions
# 3) Develop moving process: actual changing the data in 'rows' & analazying every available attacking move.
#    Go back to the start and provide highlighting all the threating figures with every new move.


# 1 и 4:
# 	При выборе фигуры просчитываются технические, а затем особенные ходы. Технические — готовый словарь.
# 	Особенные — рокировка и двойной ход пешки. Далее возможные ходы сверяются с полем: если препятствий нет,
# 	для пешки можно кого-то атаковать на её диагонали, ход находится в рамках поля,
# 	то ход добавляется в финальный словарь. В словаре 2 поля: ‘attack’ и ‘move’.
# 2:
# 	В самом начале хода отрисовка поля производится с подсвечиванием фигур под боем.
# 	Если предупреждающий словарь этой команды пуст, то орисовка без подсвечиваний.
# 	В противном случае нужные фигуры подсвечиваются красным.
#
# Ход(2):
# После движения по доске просчитываются возможные ходы из текущей позиции.
# Каждый «атакующий» возможный ход записывать в предупреждающий словарь.
# Для каждой стороны — свой словарь. В нём ключи — фигуры противника, а значения — собственные фигуры,
# находящиеся под боем. Словарь пополняется после хода противника. Каждый раз, когда противник выбирает фигуру,
# текущие предупреждения сбрасываются, а появляются новые после совершённого хода.
# 3:
# 	Если под боем оказывается король, то включается  checkMode. В нём первым делом вызывается функция isCheckmate,
# 	которая проверяет возможные пути уйти из под шаха.

class Board():
    def __init__(self):
        self.rows = {8: ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                     7: ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                     6: ['.'] * 8, 5: ['.'] * 8, 4: ['.'] * 8, 3: ['.'] * 8,
                     2: ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                     1: ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']}
        self.turn = "white"
        self.winner = None

    @property
    def available_positions(self):
        figures = ['r', 'n', 'b', 'q', 'k', 'p']
        trans = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        result = []
        for row in self.rows:
            currentRow = self.rows[row]
            for i, el in enumerate(currentRow):
                if el in [l.upper() for l in figures] and self.turn == 'white':
                    result.append(trans[i] + str(row))
                elif el in figures and self.turn == 'black':
                    result.append(trans[i] + str(row))
        return result


    def printBoard(self):
        clean()
        print('\033[40m' + '   ' + 'A B C D E F G H' + '   ' + '\033[0m')
        for row in self.rows:
            print('\033[40m' + str(row) + '\033[0m', end='  ')
            for el in self.rows[row]:
                print(el, end=' ')
            print(' ' + '\033[40m' + str(row) + '\033[0m', )
        print('\033[40m' + '   ' + 'A B C D E F G H' + '   ' + '\033[0m')

    @staticmethod
    def clean():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    @property
    def localized_turn(self) -> str:
        if self.turn == 'white':
            return 'Белых'
        else:
            return 'Чёрных'

    def changeTurn(self):
        if self.turn == 'white':
            self.turn = "black"
        else:
            self.turn = 'white'


# moves_history = {'r1': 0, 'n1': 0, 'b1': 0, 'q': 0, 'k': 0, 'b2': 0, 'n2': 0, 'r2': 0,
#                  'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0, 'p5': 0, 'p6': 0, 'p7': 0, 'p8': 0,
#                  'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0, 'P5': 0, 'P6': 0, 'P7': 0, 'P8': 0,
#                  'R1': 0, 'N1': 0, 'B1': 0, 'Q': 0, 'K': 0, 'B2': 0, 'N2': 0, 'R2': 0}
# turn = "white"
#
#
# def getCurrentTurn() -> str:
#     if turn == 'white':
#         return 'Белых'
#     else:
#         return 'Чёрных'
#

def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#
#
# def changeTurn():
#     global turn
#     if turn == 'white':
#         turn = 'black'
#     else:
#         turn = 'white'
#
#
# def printBoard():
#     clean()
#     print('\033[40m' + '   ' + 'A B C D E F G H' + '   ' + '\033[0m')
#     # for el in rows:
#     #     print(el, '', *rows[el], '', el)
#     for row in rows:
#         print('\033[40m' + str(row) + '\033[0m', end='  ')
#         for el in rows[row]:
#             print(el, end=' ')
#         print(' ' + '\033[40m' + str(row) + '\033[0m', )
#     print('\033[40m' + '   ' + 'A B C D E F G H' + '   ' + '\033[0m')
#
#
# def getXYcords(cord) -> tuple:
#     y = int(cord[1])
#     letter_cord = cord[0].lower()
#     letters_dict = {
#         'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8
#     }
#     return letters_dict[letter_cord], y
#
#
# def getFinishCord() -> tuple:
#     while True:
#         try:
#             finishCord = input("Введите позицию, куда переставить фигуру(e.g. a3): ")
#             if (finishCord[0].lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#                     or finishCord[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']):
#                 raise ValueError
#
#         except ValueError:
#             printBoard(rows)
#             print("Введена неккоректная позиция! Попробуйте ещё раз")
#             continue
#
#         return getXYcords(finishCord)
#
#
# def moveFigure(f, x, y):
#     pass


def main():
    # TODO
    # 2) Choosen figure -> refresh, highlight
    board = Board()
    err_msg = ''
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    digits = ['1', '2', '3', '4', '5', '6', '7', '8']
    while board.winner is None:
        board.printBoard()
        print(err_msg, end='')
        print(f'Ход {board.localized_turn}')

        try:

            fig = input("Введите позицию фигуры (e.g. A2/E7): ")
            if fig[0].upper() not in letters or fig[1] not in digits or fig not in board.available_positions:
                raise NameError

            cord = input("Введите позицию хода (e.g. E4/A3): ")
            if (cord[0].upper() not in letters or cord[1] not in digits):
                raise ValueError


        except NameError:
            err_msg = 'Введена неккоректная фигура! Попробуйте ещё раз\n'
            continue

        except ValueError:
            err_msg = 'Введена неккоректная позиция! Попробуйте ещё раз\n'
            continue

        i = input()
        err_msg = ''
        board.changeTurn()

    # error_type = None
    # while True:
    #     printBoard()
    #     print(f'Ход {getCurrentTurn()}')
    #     if error_type == 'value':
    #         print('Введена неккоректная команда! Попробуйте ещё раз')
    #         error_type = None
    #
    #     # check for correct input
    #     try:
    #         fig, cord = map(str, input("Введите фигуру и её позицию (e.g. p e4): ").split())
    #
    #         if (fig.lower() not in ['p', 'q', 'k', 'b', 'n', 'r']
    #                 or cord[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']
    #                 or cord[0].lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
    #             raise ValueError
    #
    #     except ValueError:
    #         error_type = 'value'
    #         continue
    #
    # get available moves & color probable pos
    # steps = get_possible_steps(fig, *getXYcords(cord))
    # highlightAvailableMoves(steps)
    # for move in steps:
    #     print(rows[move[1]][move[0] - 1])
    # finishCord = getFinishCord()
    #
    # changeTurn()


main()
