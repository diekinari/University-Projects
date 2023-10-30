import csv
import pickle
import tables

# a = [
#     [3, 2, 1],
#     [6, 5, 4],
#     [9, 8, 7]
# ]
# l = []
# for row in a:
#     print(row)
#     l.append()
# print(l)

# db = [['имя', 'уровень', 'бюджет'], ['данек', 2, 58830],['мрак', 48, 3994]]

# with open('data.txt', 'w') as file:
#     for row in db:
#         newRow = ''
#         for i in range(len(row)):
#             if len(row)-1 > i > 0 :
#                 newRow += ' ' + str(row[i]) + ' '
#             elif i == 0:
#                 newRow += str(row[i])
#             else:
#                 newRow += str(row[i]) + '\n'
#         file.write(newRow)

# file.write(str([str(el).strip('[],') for el in str(row).split()]))


tbl = tables.Table()
tbl.load_table('data.txt')
tbl.print_table()
print(tbl.get_column_types())
