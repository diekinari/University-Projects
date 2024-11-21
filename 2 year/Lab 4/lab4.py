import tkinter as tk
from time import sleep
from tkinter import messagebox
import random

class Cell:
    def __init__(self, master, x, y):
        self.master = master
        self.x = x
        self.y = y
        self.is_mine = False
        self.is_open = False
        self.is_flagged = False
        self.button = tk.Button(master, width=2, height=1, command=self.open_cell)
        self.button.bind('<Control-Button-1>', self.toggle_flag)
        self.button.grid(row=y, column=x)

    def open_cell(self):
        if self.is_open or self.is_flagged:
            return
        if not self.master.mines_placed:
            self.master.place_mines(self.x, self.y)
        self.is_open = True
        if self.is_mine:
            self.button.config(text="💣")
            self.master.game_over(False)
        else:
            mines_around = self.master.count_mines_around(self.x, self.y)
            if mines_around > 0:
                self.button.config(text=str(mines_around))
            else:
                self.master.open_adjacent_cells(self.x, self.y)
            self.master.check_win()

    def toggle_flag(self, event):
        if not self.is_open:
            if not self.is_flagged:
                if self.master.flag_count < self.master.mines:
                    self.is_flagged = not self.is_flagged
                    self.master.flag_count += 1
                    self.button.config(text="🚩")
            else:
                self.is_flagged = not self.is_flagged
                self.master.flag_count -= 1
                self.button.config(text="")




class MinesweeperGame(tk.Frame):
    def __init__(self, master, rows=10, columns=10, mines=10):
        super().__init__(master)
        self.master = master
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.flag_count = 0
        self.cells = []
        self.mine_positions = []
        self.mines_placed = False
        self.init_game()

    def init_game(self):
        self.pack()
        self.master.title("Сапёр")
        self.create_board()

    def create_board(self):
        for y in range(self.rows):
            row = []
            for x in range(self.columns):
                cell = Cell(self, x, y)
                row.append(cell)
            self.cells.append(row)

    def place_mines(self, exclude_x, exclude_y):
        # Собрать все возможные позиции для мин, исключая первую ячейку и её соседей
        possible_positions = [
            (x, y) for x in range(self.columns) for y in range(self.rows)
            if (x, y) not in [(exclude_x + dx, exclude_y + dy)
                              for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                              if 0 <= exclude_x + dx < self.columns and 0 <= exclude_y + dy < self.rows]
        ]
        if self.mines > len(possible_positions):
            raise ValueError("Слишком много мин для заданного размера поля.")
        self.mine_positions = random.sample(possible_positions, self.mines)
        for x, y in self.mine_positions:
            self.cells[y][x].is_mine = True
        self.mines_placed = True

    def count_mines_around(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.columns and 0 <= ny < self.rows and self.cells[ny][nx].is_mine:
                    count += 1
        return count

    def open_adjacent_cells(self, x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.columns and 0 <= ny < self.rows:
                    cell = self.cells[ny][nx]
                    if not cell.is_open and not cell.is_mine:
                        cell.open_cell()


    def check_win(self):
        for row in self.cells:
            for cell in row:
                if not cell.is_mine and not cell.is_open:
                    return
        self.game_over(True)


    def game_over(self, win):
        for x, y in self.mine_positions:
            self.cells[y][x].button.config(text="💣")
        self.master.after(500, self.show_game_over_message, win)

    def show_game_over_message(self, win):
        messagebox.showinfo("Сапёр", "Вы выиграли!" if win else "Вы проиграли!")
        self.master.destroy()


def main():
    root = tk.Tk()
    MinesweeperGame(root, rows=10, columns=10, mines=15)
    root.mainloop()

if __name__ == "__main__":
    main()
