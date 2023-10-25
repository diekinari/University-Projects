import csv
import pickle


class Table:

    def __init__(self):
        self.type = None
        self.data = []
        self.name = ''

    def load_table(self, filePath):

        def load_csv():
            try:
                with open(filePath, 'r') as file:
                    csv_reader = csv.reader(file)
                    self.data = [row for row in csv_reader]
            except FileNotFoundError:
                print('Файл не найден!')

        def load_txt():
            try:
                with open(filePath, 'r') as file:
                    self.data = [row.split() for row in file.readlines()]
            except FileNotFoundError:
                print('Файл не найден!')

        def load_pkl():
            try:
                with open(filePath, 'rb') as file:
                    self.data = pickle.load(file)
            except FileNotFoundError:
                print('Файл не найден!')

        try:
            assert filePath[-3:] in ['csv', 'txt', 'pkl'], 'Неподходящий формат файла!'
            self.name = filePath[:-4]
            if filePath[-3:] == 'csv':
                self.type = 'csv'
                load_csv()
            elif filePath[-3:] == 'txt':
                self.type = 'txt'
                load_txt()
            elif filePath[-3:] == 'pkl':
                self.type = 'pkl'
                load_pkl()
        except AssertionError as msg:
            print(msg)

    def save_table(self, name=''):
        if name == '':
            name = self.name

        def save_csv():
            with open(name + '.' + self.type, 'w') as file:
                csv.writer(file).writerows(self.data)

        def save_txt():
            with open(name + '.' + self.type, 'w') as file:
                for row in self.data:
                    newRow = ''
                    for i in range(len(row)):
                        if len(row) - 1 > i > 0:
                            newRow += ' ' + str(row[i]) + ' '
                        elif i == 0:
                            newRow += str(row[i])
                        else:
                            newRow += str(row[i]) + '\n'
                    file.write(newRow)

        def save_pkl():
            with open(name + '.' + self.type, 'wb') as file:
                pickle.dump(self.data, file)

        try:
            assert not (any(el in name for el in
                            ['<', '>', ':', '"', '/', '\\', '|', '?', '*', ' ', '.'])), 'Неккоректное имя файла!'
            if self.type == 'csv':
                save_csv()
            elif self.type == 'txt':
                save_txt()
            elif self.type == 'pkl':
                save_pkl()

        except AssertionError as msg:
            print(msg)

    def print_table(self):
        for i in range(len(self.data)):
            newRow = ''
            for j in range(len(self.data[i])):
                if j == 0:
                    newRow += str(self.data[i][j])
                else:
                    prevColumn = [str(row[j-1]) for row in self.data]
                    maxPrevColumnWord = max(prevColumn, key=len)
                    prevWordInThisRow = str(self.data[i][j-1])
                    newRow += (len(maxPrevColumnWord) - len(prevWordInThisRow) + 1) * ' ' + str(self.data[i][j])
            print(newRow)

    def get_rows_by_number(self, start, stop=0, copy_table=False):
        






