import copy
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
                    prevColumn = [str(row[j - 1]) for row in self.data]
                    maxPrevColumnWord = max(prevColumn, key=len)
                    prevWordInThisRow = str(self.data[i][j - 1])
                    newRow += (len(maxPrevColumnWord) - len(prevWordInThisRow) + 1) * ' ' + str(self.data[i][j])
            print(newRow)

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        result = []
        if not stop:
            stop = start
        for i in range(start - 1, stop):
            try:
                result.append(self.data[i])
            except IndexError:
                print('Строк(-и) с таким номером не существует !')
        if copy_table:
            return copy.deepcopy(result)
        return result

    def get_rows_by_index(self, *args, copy_table=False):
        try:
            mArgs = [str(arg) for arg in args]
            firstColumn = [str(row[0]) for row in self.data]

            assert all(el in firstColumn for el in mArgs), 'Некорректные аргументы!'
            result = [row for row in self.data if str(row[0]) in mArgs]

            if copy_table:
                return copy.deepcopy(result)
            return result
        except AssertionError as msg:
            print(msg)

    def get_column_types(self, by_number=True):
        result = {}
        for i in range(len(self.data[0])):
            if by_number:
                result[i+1] = type(self.data[1][i])
            else:
                result[self.data[0][i]] = type(self.data[1][i])
        return result




