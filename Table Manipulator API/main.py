import csv
import pickle
import tables

# a = [
#     [3, 2, 1],
#     [6, 5, 4],
#     [9, 8, 7]


tbl = tables.Table()
tbl.load_table('data.txt')
# tbl.print_table()
data = tbl.data
print(tbl.get_columns_types(by_number=True))


# def getColumnTypes(column):
#     result = []
#     for i in range(1, len(column)):
#         if column[i].isnumeric():
#             element_type = 'int'
#         elif column[i] in ['True', 'False']:
#             element_type = 'bool'
#         elif ''.join(column[i].split('.')).isnumeric():
#             element_type = 'float'
#         else:
#             element_type = 'str'
#
#         result.append(element_type)
#
#     return result
#
#
# def areTypesAlike():
#     statementsList = []  # [areAllTheTypesInColumn0TheSame, ...]
#     for i in range(len(data[0])):
#         currentColumn = [data[x][i] for x in range(len(data[0]))]
#         types = getColumnTypes(currentColumn)
#         statementsList.append(all([types[i] == types[i+1] for i in range(len(types) - 1)])) # check for every type in cur column is the same
#
#     return all(statementsList)
#
#
# print(areTypesAlike())
