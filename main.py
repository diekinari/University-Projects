import itertools
# task 14 var 8
# def SumRange(a, b):
#     result = 0
#     if a > b:
#         return 0
#     for x in range(a, b + 1):
#         result += x
#     return result
#
#
# print(SumRange(1, 5))
# print(SumRange(5, 10))



# task 15
# def RemoveRows(matrix, k1, k2):
#     end = k2
#     if k1 > len(matrix):
#         return
#     elif k2 > len(matrix):
#         end = len(matrix)
#     tempMatrix = [matrix[x] for x in range(k1 - 1, end)]
#     for el in tempMatrix:
#         matrix.remove(el)
#
#
# m = [[1, 2, 3], [3, 2, 1], [5, 6, 7], [7, 8, 9]]
# RemoveRows(m, 3, 4)
# print(m)

# task 16
# a
# def secondIsBigger(list1, list2):
#     return [x for x in itertools.product(list1, list2) if x[0] < x[1]]
#
#
# def fusual(list1, list2):
#     return [x for x in itertools.product(list1, list2)]
#
#
# def main(list1, list2, criteria=fusual):
#     print(criteria(list1, list2))
#
#
# a = [1, 2, 3, 4, 5]
# b = [3, 2, 1]
# main(a, b)
# main(a, b, secondIsBigger)

#b
# def main(sList, separator=None):
#     if separator:
#         result = []
#         for s in sList:
#             currS = set(s)
#             newS = ''
#             for symb in currS:
#                 newS += symb + separator
#                 print(newS)
#             newS = newS.strip(separator)
#             result.append(newS)
#
#         return result
#     else:
#         return sList
# l = ['abcdef', 'qqwertyeqwe', 'xzxqwertc', '12345677654321']
# print(main(l, ';'))
# print(main(l))
# c
# def onlyUpper(sList):
#     return [el for el in sList if el.isupper()]
#
# data = ['qwerty', 'QWERTY', 'QWErty', 'zxcvb', 'ZXCvb', 'ZXCVB']
# print(onlyUpper(data))

#d
# def uniqueElements(*args):
#     result = set()
#     for el in args:
#         for symb in el:
#             result.add(symb)
#     return list(result)
#
# test1 = ['a', 'b', 'c', 'd']
# test2 = ['b', 'c', 'd', 'e']
# test3 = ['c', 'd', 'e', 'f']
# print(uniqueElements(test1, test2, test3))

# task 17
# def digits(s, count=0, index=0):
#     if index < len(s):
#         if s[index].isdigit():
#             return digits(s, count+1, index+1)
#         else:
#             return digits(s, count, index+1)
#     else:
#         return count
#
#
# s = 'r1t2y3y4y5y6y7y8' # 8
# print(digits(s))

# task 18
# def sum_vectors(args):
#     x = 0
#     y = 0
#     z = 0
#     for i in range(len(args)):
#         x += args[i][0]
#         y += args[i][1]
#         z += args[i][2]
#     return (x, y, z)
#
#
# def vector_times_digit(vector, digit):
#     res = []
#     for i in range(len(vector)):
#         res.append(vector[i] * digit)
#     return res
#
#
# def find_min_and_max(vector):
#     return [min(vector), max(vector)]
#
# vectors = [[1, 5, 7], [2, 4, -2], [1, 1, 1]]
# print(sum_vectors(vectors))
# print(vector_times_digit([1, 5, 10], 6))
# print(find_min_and_max([4, 13, 27]))