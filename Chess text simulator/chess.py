import os

rows = {8: ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        7: ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        6: ['.'] * 8, 5: ['.'] * 8, 4: ['.'] * 8, 3: ['.'] * 8,
        2: ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        1: ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']}
turn = "white"


def getCurrentTurn():
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


def printBoard(board):
    clean()
    print('   A B C D E F G H  ')
    for el in board:
        print(el, '', *board[el], '', el)
    print('   A B C D E F G H  ')


def get_possible_steps(fig, x, y):
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

    global pos_field
    variants_unchecked = {
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

    fig_steps = variants_unchecked[fig]
    variants_checked = []

    for comb in fig_steps:
        # проверка на фигуру в клетке

        if 1 <= comb[1] <= 8 and 0 <= comb[1] <= 7:
            print(comb[1], comb[0])
            fig_in_cell = pos_field[comb[1]][comb[0]]

            if fig_in_cell == '.':
                variants_checked.append(comb)

            elif fig_in_cell != '.' and fig_in_cell.isupper() == fig.isupper():
                variants_checked.append(comb)


    return variants_checked


def main():
    try:
        while True:
            printBoard(rows)
            print(f'Ход {getCurrentTurn()}')
            fig, cord = map(str, input("Введите фигуру и её позицию (e.g. p e4): ").split())
            # check correct name & get available moves & color probable pos


            changeTurn()
            # check for correct input
    except:
        pass


main()
