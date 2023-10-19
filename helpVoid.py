# command = [9, 'минус', 7, 'умножить', 5, 'плюс', 2, 'разделить', 2, 'разделить', 9]
# # 4.23 - 56 * 20 / 9 - 6
# # 4.23 56 20 умножить 9 разделить минус 6 минус
# priorities = {'умножить': 2, "разделить": 2, "плюс": 1, "минус": 1}
# postfixCommand = []
# stack = []
# # stack.sort(key=lambda x: priorities[x], reverse=True)
# operator = {'плюс': lambda x, y: x + y,
#             'минус': lambda x, y: x - y,
#             'умножить': lambda x, y: x * y,
#             'разделить': lambda x, y: x / y}
#
# for el in command:
#     if type(el) in [int, float]:
#         postfixCommand.append(el)
#     else:
#         if len(stack) == 0:
#             stack.append(el)
#         else:
#             if priorities[el] > priorities[stack[-1]]:
#                 stack.append(el)
#             else:
#                 for op in stack[::-1]:
#                     if priorities[op] >= priorities[el]:
#                         postfixCommand.append(op)
#                         stack.remove(op)
#                 stack.append(el)
# postfixCommand += [stack[i] for i in range(len(stack) - 1, -1, -1)]
#
# resultStack = []
# for element in postfixCommand:
#     if type(element) in [int, float]:
#         resultStack.append(element)
#     else:
#         resultStack.append(operator[element](resultStack[-2], resultStack[-1]))
#         resultStack.pop(-2)
#         resultStack.pop(-2)
# answer = round(resultStack[0], 3)
# print(answer)
#
import csv
import pickle

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


with open('noski.txt', 'w') as file:
    newRow = []
    for row in a:
        pass
        # for i in range(1, len(row)-2):
        #     newRow.append(str(row[i]) + ' ' + str(row[i+1]))
    newRow.append('\n')
    print(newRow)
        # file.writelines([str(x) for x in row])

