import csv
import pickle


# TODO
# 1) Implement load/save table data with exceptions


class Table():

    def __init__(self):
        self.type = None
        self.data = []

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
                    csv_reader = csv.reader(file)
                    self.data = [row for row in csv_reader]
            except FileNotFoundError:
                print('Файл не найден!')

        try:
            assert filePath[-3:] in ['csv', 'txt', 'pkl'], 'Неподходящий формат файла!'
            if filePath[-3:] == 'csv':
                self.type = 'csv'
                load_csv()
            elif filePath[-3:] == 'txt':
                self.type = 'txt'
                print("it's txt-type file")
            elif filePath[-3:] == 'pkl':
                print("it's pickle-type file")
        except AssertionError as msg:
            print(msg)


tbl = Table()
tbl.load_table('noski.csg')
print(tbl.data)

# with open('noski.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['nosochek1', 'nosochek2', 'nosochek3'])
#     csv_writer.writerow(['nosochek4', 'nosochek5', 'nosochek6'])
