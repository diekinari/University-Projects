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



rows = {8: ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        7: ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        6: ['.'] * 8, 5: ['.'] * 8, 4: ['.'] * 8, 3: ['.'] * 8,
        2: ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        1: ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']}
moves_history = {'r1': 0, 'n1': 0, 'b1': 0, 'q': 0, 'k': 0, 'b2': 0, 'n2': 0, 'r2': 0,
                 'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0, 'p5': 0, 'p6': 0, 'p7': 0, 'p8': 0,
                 'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0, 'P5': 0, 'P6': 0, 'P7': 0, 'P8': 0,
                 'R1': 0, 'N1': 0, 'B1': 0, 'Q': 0, 'K': 0, 'B2': 0, 'N2': 0, 'R2': 0}
turn = "white"


def getCurrentTurn() -> str:
    if turn == 'white':
        return 'Белых'
    else:
        return 'Чёрных'


def changeTurn():
    global turn
    if turn == 'white':
        turn = 'black'
    else:
        turn = 'white'


def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def printBoard():
    clean()
    print('\033[40m' + '   ' + 'A B C D E F G H' +  '   ' + '\033[0m')
    # for el in rows:
    #     print(el, '', *rows[el], '', el)
    for row in rows:
        print('\033[40m' + str(row) + '\033[0m', end='  ')
        for el in rows[row]:
            print(el, end=' ')
        print(' ' + '\033[40m' + str(row) + '\033[0m',)
    print('\033[40m' + '   ' + 'A B C D E F G H' +  '   ' + '\033[0m')

def getXYcords(cord) -> tuple:
    y = int(cord[1])
    letter_cord = cord[0].lower()
    letters_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8
    }
    return letters_dict[letter_cord], y

def get_possible_steps(fig, x, y) -> list:
    def queen_moves(x, y):
        var_moves = []

        # horizontal + vertical
        for i in range(8):

            if i != x:
                var_moves.append([i, y])

            if i != y:
                var_moves.append([x, i])

        # diagonal
        for i in range(1, 8):
            if 0 <= x + i < 8 and 0 <= y + i < 8:
                var_moves.append([x + i, y + i])

            if 0 <= x - i < 8 and 0 <= y - i < 8:
                var_moves.append([x - i, y - i])

            if 0 <= x + i < 8 and 0 <= y - i < 8:
                var_moves.append([x + i, y - i])

            if 0 <= x - i < 8 and 0 <= y + i < 8:
                var_moves.append([x - i, y + i])

        return var_moves

    def rook_moves(x, y):

        var_moves = []

        for i in range(8):

            if i != x:
                var_moves.append([i, y])

            if i != y:
                var_moves.append([x, i])

        return var_moves

    def bishop_moves(x, y):

        var_moves = []

        for i in range(1, 8):
            if 0 <= x + i < 8 and 0 <= y + i < 8:
                var_moves.append([x + i, y + i])

            if 0 <= x - i < 8 and 0 <= y - i < 8:
                var_moves.append([x - i, y - i])

            if 0 <= x + i < 8 and 0 <= y - i < 8:
                var_moves.append([x + i, y - i])

            if 0 <= x - i < 8 and 0 <= y + i < 8:
                var_moves.append([x - i, y + i])

        return var_moves

    based_moves = {
        'P': [[x, y + 1], [x, y + 2]],
        'K': [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y + 1], [x + 1, y - 1], [x + 1, y],
              [x + 1, y + 1]],
        'Q': queen_moves(x, y),
        'N': [[x + 1, y + 2], [x + 1, y - 2], [x - 1, y + 2], [x - 1, y - 2], [x + 2, y + 1], [x + 2, y - 1],
              [x - 2, y + 1], [x - 2, y - 1]],
        'R': rook_moves(x, y),
        'B': bishop_moves(x, y),

        'p': [[x, y - 1], [x, y - 2]],
        'k': [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y - 1], [x, y + 1], [x + 1, y - 1], [x + 1, y],
              [x + 1, y + 1]],
        'q': queen_moves(x, y),
        'n': [[x + 1, y + 2], [x + 1, y - 2], [x - 1, y + 2], [x - 1, y - 2], [x + 2, y + 1], [x + 2, y - 1],
              [x - 2, y + 1], [x - 2, y - 1]],
        'r': rook_moves(x, y),
        'b': bishop_moves(x, y)
    }


    return based_moves[fig]
    # fig_steps = variants_unchecked[fig]
    # variants_checked = []
    #
    # for comb in fig_steps:
    #     # проверка на фигуру в клетке
    #
    #     if 1 <= comb[1] <= 8 and 0 <= comb[1] <= 7:
    #         print(comb[1], comb[0])
    #         fig_in_cell = pos_field[comb[1]][comb[0]]
    #
    #         if fig_in_cell == '.':
    #             variants_checked.append(comb)
    #
    #         elif fig_in_cell != '.' and fig_in_cell.isupper() == fig.isupper():
    #             variants_checked.append(comb)
    #
    # return variants_checked

def getFinishCord() -> tuple:
    while True:
        try:
            finishCord = input("Введите позицию, куда переставить фигуру(e.g. a3): ")
            if (finishCord[0].lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                    or finishCord[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']):
                raise ValueError

        except ValueError:
            printBoard(rows)
            print("Введена неккоректная позиция! Попробуйте ещё раз")
            continue

        return getXYcords(finishCord)

def moveFigure(f, x, y):
    pass

def main():
    error_type = None
    while True:
        printBoard()
        print(f'Ход {getCurrentTurn()}')
        if error_type == 'value':
            print('Введена неккоректная команда! Попробуйте ещё раз')
            error_type = None

        # check for correct input
        try:
            fig, cord = map(str, input("Введите фигуру и её позицию (e.g. p e4): ").split())

            if (fig.lower() not in ['p', 'q', 'k', 'b', 'n', 'r']
                    or cord[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']
                    or cord[0].lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
                raise ValueError

        except ValueError:
            error_type = 'value'
            continue

        # get available moves & color probable pos
        steps = get_possible_steps(fig, *getXYcords(cord))
        highlightAvailableMoves(steps)
        for move in steps:
            print(rows[move[1]][move[0] - 1])
        # finishCord = getFinishCord()

        changeTurn()


main()
