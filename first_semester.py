import itertools
import re
import vectorsLib
import os
import collections
import enum


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

# b
# def main(sList, separator=None):
#     if separator:
#         result = []
#         for s in sList:
#             currS = set(s)
#             newS = ''
#             for symb in currS:
#                 newS += symb + separator
#
#             newS = newS.strip(separator)
#             result.append(newS)
#
#         return result
#     else:
#         return ' '.join(sList)
# l = ['abcdef', 'qqwertyeqwe', 'xzxqwertc', '12345677654321']
# print(main(l, ';'))
# print(main(l))
# c
# def onlyUpper(sList):
#     return [el for el in sList if el.isupper()]
#
# data = ['qwerty', 'QWERTY', 'QWErty', 'zxcvb', 'ZXCvb', 'ZXCVB']
# print(onlyUpper(data))

# d
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
# s = 'r1t2y3y4y5y6y7y' # 8
# print(digits(s))

# task 18
# vectors = [[1, 5, 7], [2, 4, -2], [1, 1, 1]]
# print(vectorsLib.sum_vectors(vectors))
# print(vectorsLib.vector_times_digit([1, 5, 10], 6))
# print(vectorsLib.find_min_and_max([4, 13, 27]))

# task 19
# s = '!abcd3535!'
# with open('19.txt', 'r+') as file:
#     content = file.read()
#     content = re.sub('\n\s*\n', '\n' + s + '\n', content)
#     file.seek(0)
#     file.write(content)

# task 20
# with open("f.txt", "r") as file:
#     data = list(map(int, file.read().split()))
#
# even_nums = [number for number in data if number % 2 == 0]
#
# with open("g.txt", "w") as file:
#     file.write(" ".join(str(number) for number in even_nums))

# task 21 START HERE

# 1 2 3 4
# 6 7 8 9
# 9 8 7 6
# 0 1 9 2
#
# 8 3 7 2
# 5 2 9 1
# 3 1 4 2
# 7 7 9 4
#

# def transpose(matrix):
#     return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
#
#
# file1 = open("input.txt", "r+")
# file2 = open("output.txt", "w")
# currentMatrix = []
# matrixes = []
#
# for line in file1:
#     # if not empty space
#     if not re.fullmatch('\s*', line):
#         currentMatrix.append(line.strip().split())
#     else:
#         matrixes.append(currentMatrix)
#         currentMatrix = []
# file1.seek(0)
# for currentMatrix in matrixes:
#     if sum(int(currentMatrix[i][i]) for i in range(len(currentMatrix))) % 2 != 0:
#         file2.writelines([' '.join(currentMatrix[i]) + '\n' for i in range(len(currentMatrix))])
#         file2.write('\n')
#         file1.writelines([' '.join(transpose(currentMatrix)[i]) + '\n' for i in range(len(currentMatrix))])
#         file1.write('\n')
#
# file1.close()
# file2.close()

# task 22
# a
# def find_words(s):
#     consonants = 'бвгджзйклмнпрстфхцчшщ'
#     words = re.findall('\w+', s)
#     res = []
#     for word in words:
#         if word[0].lower() in consonants:
#             res.append(word)
#     return res
#
#
# s = input("Введите предложение: ")
# result = find_words(s)
# print(result)

# Каждый охотник желает автор где источник фазан
# b
# with open('phone_numbers.txt', 'r') as file:
#     content = file.read()
#     pattern = r"[78]\d{3}\d{3}\d{2}\d{2}"
#     for num in re.finditer(pattern, content):
#         print(num.group())

# task 23
# a
# try:
#     # file1 = open('nonexistent.txt', 'r')
#     file2 = open('23.txt', 'r')
#     if file2.read():
#         print('Файл успешно открыт')
#     else:
#         raise EOFError
# except FileNotFoundError:
#     print('Файл не найден')
# except EOFError:
#     print("Файл пустой")
# b
# try:
#     s = input()
#     pattern = '((http|https)\:\/\/[a-zA-Z0-9\.\-]+\.[a-z]{2,3}(\/[\w\-]+)*)'
#     assert re.match(pattern, s), 'Строка НЕ является URL-адресом'
#     print('Строка является URL-адресом')
# except AssertionError as msg:
#     print(msg)
# c
# try:
#     p = '23.txt'
#     assert os.path.exists('23.txt'), "Файл не найден"
#     with open(p, 'r') as file:
#         assert file.read(), 'Файл пустой'
#         print('Файл успешно открыт')
# except AssertionError as msg:
#     print(msg)

# task 24
# a
# with open('text.txt', 'r') as file:
#     c = collections.Counter()
#     text = file.read()
#     for word in text.split():
#         c[word] += 1
#     print(c)
# b

# def main(numsList):
#     c = collections.defaultdict(int)
#     for num in numsList:
#         c[num] += 1
#     return c
#
#
# print(main([1, 1, 23, 4, 3, 13, 23, 1, 5, 9, 3, 4, 0, 5, 9, 23, 5]))

# c
# class Sports(enum.Enum):
#     soccer = 11
#     basketball = 11
#     hockey = 20
#     voleyball = 6
#
#
# def getPlayersNumber(sport):
#     for field in Sports:
#         if field.name == sport:
#             return field.value
#
#
# print(getPlayersNumber('voleyball'))

# d
# def unique(strings):
#     s = set()
#     for st in strings:
#         s.update(st.split())
#     return frozenset(s)
#
#
# strings = ['Hello World', 'Hello Universe', 'Goodbye World', 'GoodBye Universe']
# print(unique(strings))

# e
# def getAlbumsBefore80s(albums):
#     result = []
#     for album in albums:
#         if album.release_date < 1980:
#             result.append(album)
#     return result
#
#
# Album = collections.namedtuple('Album', ['name', 'release_date', 'ratings', 'sales'])
# print(getAlbumsBefore80s([Album('Thriller', 1982, 5, 100000000), Album('Abbey Road', 1969, 99, 6000000),
#                           Album('Born in the USA', 1984, 8.5, 14000000),
#                           Album('The Dark Side of the Moon', 1973, 9, 50000000),
#                           Album('Back in Black', 1980, 75, 50000000)]))

# f
# def getInfo():
#     with open('goods&prices.txt', 'r') as file:
#         d = collections.OrderedDict()
#         for line in file.readlines():
#             good, price = line.split()
#             d[good] = price
#     return collections.OrderedDict(sorted(d.items()))
#
#
# print(getInfo())
