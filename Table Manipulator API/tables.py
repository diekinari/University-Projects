import copy
import csv
import pickle


def getColumnTypes(column):
    result = []
    for i in range(1, len(column)):
        if column[i].isnumeric():
            element_type = 'int'
        elif column[i] in ['True', 'False']:
            element_type = 'bool'
        elif ''.join(column[i].split('.')).isnumeric():
            element_type = 'float'
        else:
            element_type = 'str'

        result.append(element_type)

    return result


def areTypesInAllColumnsAlike(data):
    statementsList = []  # [areAllTheTypesInColumn0TheSame, ...]
    for i in range(len(data[0])):
        currentColumn = [data[x][i] for x in range(len(data))]
        types = getColumnTypes(currentColumn)
        statementsList.append(all([types[x] == types[x + 1] for x in
                                   range(len(types) - 1)]))  # check for every type in cur column is the same

    return all(statementsList)


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

    def get_columns_types(self, by_number=False):
        try:
            assert areTypesInAllColumnsAlike(self.data), 'Типы данных в каком-то столбце не совпадают !'
            result = {}
            for i in range(len(self.data[0])):  # going through columns' names
                currentColumn = [self.data[x][i] for x in range(len(self.data))]
                currentType = getColumnTypes(currentColumn)[0]
                if by_number:
                    result[i + 1] = currentType
                else:
                    result[self.data[0][i]] = currentType
            return result
        except AssertionError as msg:
            print(msg)
            return {}

    # TODO
    # get воспринимает все столбцы как строки и выводит "подрзаумеваемый" тип
    # 1) Переделать get под прямой вывод типов
    # 2) Додлать set по аналогии
    def set_column_types(self, types_dict, by_number=False):
        try:
            if by_number:
                assert type(list({x for x in types_dict.keys()})[
                                0]) == int, 'При таком аргументе by_number ключи должны быть цифрами!'
            else:
                assert type(list({x for x in types_dict.keys()})[
                                0]) == str, 'При таком аргументе by_number ключи должны быть словами!'
            result = {}
            for key in types_dict.keys():  # going through columns' names
                if by_number:
                    currentColumn = [self.data[x][key - 1] for x in range(len(self.data))]
                else:
                    currentColumn = [self.data[x][self.data[0].index(key)] for x in range(len(self.data))]
                for el in currentColumn[1:]:
                    pass
                    # el = types_dict[key](el)
                print(currentColumn)


        except AssertionError as msg:
            print(msg)
        except IndexError:
            print('Неккоректный номер столбца!')
        except ValueError:
            print("Неккоректное название столбца!")

    def get_values(self, column=1):
        try:
            assert type(column) in [int, str], 'Неккоректный тип аргумента!'
            modifiedColumn = []
            if type(column) == int:
                if column < 1:
                    raise IndexError()
                sourceColumn = [row[column - 1] for row in self.data]
            else:
                sourceColumn = [row[self.data[0].index(column)] for row in self.data]
            sourceColumnTypes = getColumnTypes(sourceColumn)
            if len(set(sourceColumnTypes)) == 1:
                if sourceColumnTypes[0] == 'str':
                    modifiedColumn = sourceColumn[1:]
                elif sourceColumnTypes[0] == 'int':
                    modifiedColumn = [int(el) for el in sourceColumn[1:]]
                elif sourceColumnTypes[0] == 'float':
                    modifiedColumn = [float(el) for el in sourceColumn[1:]]
                elif sourceColumnTypes[0] == 'bool':
                    modifiedColumn = [bool(el) for el in sourceColumn[1:]]
            else:
                print('В строке содержатся элементы разных типов! Все элементы будут приведены к строке.')
                modifiedColumn = sourceColumn[1:]
            return modifiedColumn

        except AssertionError as msg:
            print(msg)
        except IndexError:
            print('Неккоректный индекс!')
        except ValueError:
            print('Неккоректное название столбца!')

    def get_value(self, column=1):
        try:
            assert len(self.data) == 1, 'Данный метод не подходит для заданной таблицы!'
            if column < 1:
                raise IndexError
            sourceElement = self.data[0][column - 1]
            if sourceElement.isnumeric():
                sourceElement = int(sourceElement)
            elif sourceElement in ['True', 'False']:
                sourceElement = bool(sourceElement)
            elif ''.join(sourceElement.split('.')).isnumeric():
                sourceElement = float(sourceElement)
            return sourceElement

        except AssertionError as msg:
            print(msg)
        except IndexError:
            print('Неккоректный номер столбца!')

    def set_values(self, *values, column=1):
        try:
            assert type(column) in [int, str], 'Неккоректный тип аргумента!'
            if type(column) == int:
                if column < 1:
                    raise IndexError()
                sourceColumn = [row[column - 1] for row in self.data]
                index = column - 1
            else:
                sourceColumn = [row[self.data[0].index(column)] for row in self.data]
                index = self.data[0].index(column)
            if len(sourceColumn) - 1 != len(values):
                raise ArithmeticError
            sourceColumnTypes = getColumnTypes(sourceColumn)

            def change_values_with_type(columnType):
                for i in range(1, len(self.data)):
                    row = self.data[i]
                    if columnType == 'bool':
                        newValue = bool(values[i - 1])
                    elif columnType == 'int':
                        newValue = int(values[i - 1])
                    elif columnType == 'float':
                        newValue = float(values[i - 1])
                    else:
                        newValue = str(values[i - 1])
                    row[index] = newValue

            if len(set(sourceColumnTypes)) != 1:
                print('В строке содержатся элементы разных типов! Все элементы будут приведены к строке.')
                change_values_with_type('str')
            else:
                change_values_with_type(sourceColumnTypes[0])

        except AssertionError as msg:
            print(msg)
        except IndexError:
            print('Неккоректный индекс!')
        except ValueError:
            print('Неккоректное название столбца!')
        except ArithmeticError:
            print('Количество значений аргументов не совпадает с количеством элементов в столбце!')

    def set_value(self, value, column=1):
        try:
            assert len(self.data) == 1, 'Данный метод не подходит для заданной таблицы!'
            if column < 1:
                raise IndexError
            mainRow = self.data[0]
            sourceElement = mainRow[column - 1]
            if sourceElement.isnumeric():
                mainRow[column - 1] = int(value)
            elif sourceElement in ['True', 'False']:
                mainRow[column - 1] = bool(value)
            elif ''.join(sourceElement.split('.')).isnumeric():
                mainRow[column - 1] = float(value)
            else:
                mainRow[column - 1] = str(value)



        except AssertionError as msg:
            print(msg)
        except IndexError:
            print('Неккоректный номер столбца!')
