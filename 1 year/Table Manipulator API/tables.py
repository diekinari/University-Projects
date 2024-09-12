import copy
import csv
import datetime
import pickle


def getColumnTypes(column):
    result = []
    for i in range(1, len(column)):
        result.append(type(column[i]))

    return result


def areTypesInAllColumnsAlike(data):
    statementsList = []  # [areAllTheTypesInColumn0TheSame, ...]
    for i in range(len(data[0])):
        currentColumn = [data[x][i] for x in range(len(data))]
        types = getColumnTypes(currentColumn)
        statementsList.append(all([types[x] == types[x + 1] for x in
                                   range(len(types) - 1)]))  # check if every type in cur column is the same

    return all(statementsList)


def setUpRightTypes(table):
    for i in range(len(table[0])):
        for j in range(1, len(table)):
            if '.' in table[j][i] and ''.join(table[j][i].split('.')).isnumeric():
                table[j][i] = float(table[j][i])

            elif table[j][i].isnumeric():
                table[j][i] = int(table[j][i])

            elif table[j][i] in ['True', 'False']:
                table[j][i] = bool(table[j][i])

            elif len(table[j][i].split(':')) == 3 and all([x.isnumeric() for x in table[j][i].split(':')]):
                hours, minutes, seconds = map(int, table[j][i].split(':'))
                table[j][i] = datetime.time(hours, minutes, seconds)

            elif len(table[j][i].split('-')) == 3 and all([x.isnumeric() for x in table[j][i].split('-')]):
                year, month, day = map(int, table[j][i].split('-'))
                table[j][i] = datetime.date(year, month, day)

            else:
                table[j][i] = str(table[j][i])


def concat(table1, table2):
    try:
        assert len(table1.data) == len(table2.data), 'Количество строк в таблицах не эквивалентно!'
        assert all([len(x) == len(table1.data[0]) for x in table1.data]) and all(
            [len(x) == len(table2.data[0]) for x in table2.data]), \
            'Количество стоблцов в какой-то из таблиц неккоректно!'
        for i in range(len(table1.data)):
            table1.data[i] += table2.data[i]
    except AssertionError as msg:
        print(msg)


class Table:

    def __init__(self):
        self.type = None
        self.data = []
        self.name = ''
        self.types = {}
        self.columnsCount = 0

    def load_table(self, *args, autoSetUp=False):
        def load_csv(filePath):
            try:
                with open(filePath, 'r') as file:
                    csv_reader = csv.reader(file)
                    if longMode:
                        newData = [row for row in csv_reader]
                        assert all(len(row) == self.columnsCount for row in newData), 'Структура столбцов не совпадает!'
                        self.data += newData
                    else:
                        self.data = [row for row in csv_reader]
                        self.columnsCount = len(self.data[0])
            except FileNotFoundError:
                print('Файл не найден!')

        def load_txt(filePath):
            try:
                with open(filePath, 'r') as file:
                    self.data = [row.split() for row in file.readlines()]
            except FileNotFoundError:
                print('Файл не найден!')

        def load_pkl(filePath):
            try:
                with open(filePath, 'rb') as file:
                    if longMode:
                        newData = pickle.load(file)
                        assert all(len(row) == self.columnsCount for row in newData), 'Структура столбцов не совпадает!'
                        self.data += newData
                    else:
                        self.data = pickle.load(file)
                        self.columnsCount = len(self.data[0])
            except FileNotFoundError:
                print('Файл не найден!')

        def checkTypeAndLoad(filePath):
            assert filePath[-3:] in ['csv', 'txt', 'pkl'], 'Неподходящий формат файла!'
            self.name = filePath[:-4]
            if filePath[-3:] == 'csv':
                self.type = 'csv'
                load_csv(filePath)
            elif filePath[-3:] == 'txt':
                self.type = 'txt'
                load_txt(filePath)
            elif filePath[-3:] == 'pkl':
                self.type = 'pkl'
                load_pkl(filePath)

        try:
            longMode = False
            checkTypeAndLoad(args[0])  # anyway load and process first file in the line

            if len(args) > 1:
                longMode = True
                for extraPath in args[1:]:
                    checkTypeAndLoad(extraPath)

            if autoSetUp:
                setUpRightTypes(self.data)

                try:
                    assert areTypesInAllColumnsAlike(self.data), 'Типы данных в каком-то столбце не совпадают !'
                    result = {}
                    for i in range(len(self.data[0])):  # going through columns' names
                        currentColumn = [self.data[x][i] for x in range(len(self.data))]
                        currentType = getColumnTypes(currentColumn)[0]
                        result[self.data[0][i]] = currentType
                    self.types = result
                except AssertionError as msg:
                    print(msg)

            else:
                try:
                    self.types = {key: 'type is not set' for key in self.data[0]}
                except IndexError:
                    print('Типы не могут быть установлены, так как файл не найден!')

        except AssertionError as msg:
            print(msg)

    def save_table(self, name=None, max_rows=None):
        # implement saving to a various files like *name*_*index*.*type*
        if not name:
            name = self.name

        def save_csv():
            try:
                if max_rows:
                    for i in range(len(newData)):
                        file = open(name + '_' + f'{i + 1}' + '.' + self.type, 'w')
                        csv.writer(file).writerows(newData[i])
                        file.close()
                else:
                    with open(name + '.' + self.type, 'w') as file:
                        csv.writer(file).writerows(self.data)

            except IndexError:
                print("Максимальное заданное количество рядов в новом больше, "
                      "чем количество всех рядов в исходной таблице!")

        def save_txt():
            def writeFromSource(source):
                for row in source:
                    newRow = ''
                    for i in range(len(row)):
                        if len(row) - 1 > i > 0:
                            newRow += ' ' + str(row[i]) + ' '
                        elif i == 0:
                            newRow += str(row[i])
                        else:
                            newRow += str(row[i]) + '\n'
                    file.write(newRow)

            if max_rows:
                for i in range(len(newData)):
                    file = open(name + '_' + f'{i + 1}' + '.' + self.type, 'w')
                    writeFromSource(newData[i])
                    file.close()
            else:
                file = open(name + '.' + self.type, 'w')
                writeFromSource(self.data)
                file.close()

        def save_pkl():
            try:
                if max_rows:
                    for i in range(len(newData)):
                        file = open(name + '_' + f'{i + 1}' + '.pkl', 'wb')
                        pickle.dump(newData[i], file)
                        file.close()
                else:
                    with open(name + '.pkl', 'wb') as file:
                        pickle.dump(self.data, file)

            except IndexError:
                print("Максимальное заданное количество рядов в новом больше, "
                      "чем количество всех рядов в исходной таблице!")

        try:
            if max_rows:
                max_rows = int(max_rows)
                # if len(self.data) // max_rows == len(self.data) // max_rows:
                #     filesCount = (len(self.data) // max_rows)
                # else:
                #     filesCount = (len(self.data) // max_rows) + 1

                newData = []
                tempData = []

                for r in self.data:
                    tempData.append(r)

                    if len(tempData) == max_rows:
                        newData.append(tempData)
                        tempData = []

                if len(tempData) > 0:
                    newData.append(tempData)

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
        if by_number:
            i = 1
            result = {}
            for name in self.data[0]:
                result[i] = self.types[name]
                i += 1
            return result
        else:
            return self.types

    def set_column_types(self, types_dict, by_number=False):
        try:
            if by_number:
                assert type(list({x for x in types_dict.keys()})[
                                0]) == int, 'При таком аргументе by_number ключи должны быть цифрами!'
                titles = [self.data[0][i - 1] for i in types_dict.keys()]
                for i in types_dict.keys():
                    self.types[self.data[0][i - 1]] = types_dict[i]

            else:
                assert type(list({x for x in types_dict.keys()})[
                                0]) == str, 'При таком аргументе by_number ключи должны быть словами!'
                titles = [x for x in types_dict.keys()]
                if not all(x in self.data[0] for x in titles):
                    raise ValueError
                for el in titles:
                    self.types[el] = types_dict[el]

            # for key in types_dict.keys():  # going through columns' names
            # if by_number:
            #     currentColumn = [self.data[x][key - 1] for x in range(len(self.data))]
            # else:
            #     currentColumn = [self.data[x][self.data[0].index(key)] for x in range(len(self.data))]
            # print(currentColumn)
            # for el in currentColumn[1:]:
            #     el = int(el)
            #     # el = int(el)
            #     # el = types_dict[key](el)
            # print(currentColumn)

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
                if sourceColumnTypes[0] == str:
                    modifiedColumn = sourceColumn[1:]
                elif sourceColumnTypes[0] == int:
                    modifiedColumn = [int(el) for el in sourceColumn[1:]]
                elif sourceColumnTypes[0] == float:
                    modifiedColumn = [float(el) for el in sourceColumn[1:]]
                elif sourceColumnTypes[0] == bool:
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

    def splitTable(self, rowNumber):
        try:
            return self.data[:rowNumber - 1], self.data[rowNumber - 1:]
        except AssertionError as msg:
            print(msg)
