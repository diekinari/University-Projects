import itertools
import math
import datetime
import random as rn
import numpy as np
import array
from functools import reduce


# task 25
#
#
# class Ball:
#     def __init__(self, centreCords, radius):
#         self.centreCords = centreCords
#         self.radius = radius
#
#     def countVolume(self):
#         return 4 / 3 * math.pi * self.radius ** 3
#
#     def countSquare(self):
#         return 4 * math.pi * self.radius ** 2
#
#
# myBall = Ball([1, 2, 3], 15)
# print(myBall.countSquare(), myBall.countVolume())

# task 26
# class Polynomial:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return "A - некое число, угловой коэффициент \nB - некое число, свободный член \nХ - аргумент  "
#
#     def compute(self, x):
#         return self.a * x + self.b
#
#     def find_root(self):
#         if self.b == 0:
#             return "Уравнение не линейное"
#         else:
#             return -self.b / self.a
#
#     @property
#     def square(self):
#         # Возвести многочлен в квадрат
#         return Polynomial(self.a ** 2, 2 * self.a * self.b + self.b ** 2)
#
#
# ent = Polynomial(1, 2)
# print(ent)
# print(ent.compute(2))
# print(ent.find_root())
# print(ent.square)

# task 27
# import datetime
#
#
# class Software():
#     def __init__(self, name, producer):
#         self.name = name
#         self.producer = producer
#
#     def displayInfo(self):
#         print(f'This is your {self.name} Software. It is produced by {self.producer}')
#
#     def checkUsability(self):
#         return {'status': None, 'msg': 'The usage time is not defined'}
#
#
# class Free(Software):
#     def __init__(self, name, producer):
#         super().__init__(name, producer)
#
#
# class Trial(Software):
#     def __init__(self, installationDate, trialTime, name, producer):
#         super().__init__(name, producer)
#         self.installationDate = installationDate
#         self.trialTime = trialTime
#
#     def displayInfo(self):
#         super().displayInfo()
#         print(f'Installation date: {self.installationDate}')
#         print(f'Free usage days: {self.trialTime}')
#
#     def checkUsability(self):
#         if datetime.datetime.now() < self.installationDate + datetime.timedelta(days=self.trialTime):
#             return {'status': True, 'msg': f'Today is {datetime.date.today()}. Your licence is still active !'}
#         else:
#             return {'status': False, 'msg': 'Sorry, but your free license has already expired. Buy a Commercial one!'}
#
#
# class Commercial(Software):
#     def __init__(self, installationDate, price, licenseTime, name, producer):
#         super().__init__(name, producer)
#         self.installationDate = installationDate
#         self.licenseTime = licenseTime
#         self.price = price
#
#     def displayInfo(self):
#         super().displayInfo()
#         print(f'Installation date: {self.installationDate}')
#         print(f'License usage days: {self.licenseTime}')
#         print(f'Price: {self.price}')
#
#     def checkUsability(self):
#         if datetime.datetime.now() < self.installationDate + datetime.timedelta(days=self.licenseTime):
#             return {'status': True, 'msg': f'Today is {datetime.date.today()}. Your licence is still active !'}
#         else:
#             return {'status': False, 'msg': 'Sorry, but your  license has already expired. Buy a new one!'}
#
#
# softs = [Free('Pycharm Default', 'JetBrains'),
#          Trial(datetime.datetime(2024, 2, 1), 30, 'Pycharm Medium', 'JetBrains'),
#          Commercial(datetime.datetime(2022, 1, 2), '249$', 120, 'Pycharm Business', 'JetBrains')]
#
# for soft in softs:
#     soft.displayInfo()
#     print(soft.checkUsability()['msg'])
#     print('---------------')
#
# print('!!---------!!')
#
#
# def searchAvailableSoftwares(softList):
#     for el in softList:
#         if el.checkUsability()['status']:
#             el.displayInfo()
#             print(el.checkUsability()['msg'])
#
#
# searchAvailableSoftwares(softs)

# task 28

# a
# date = datetime.datetime.now()
# current_year = lambda now_info: str(now_info).split()[0].split('-')[0]
# current_month = lambda now_info: str(now_info).split()[0].split('-')[1]
# current_date = lambda now_info: str(now_info).split()[0]
# current_time = lambda now_info: str(now_info).split()[1]
#
# print(current_year(date))
# print(current_month(date))
# print(current_date(date))
# print(current_time(date))

# b
# data = [3, -4, 5, 8, -9, 3, -8, 5, -7, 3, 1, 5, 2, 3, -4, 2]
# positive_S = lambda base_list: sum([num for num in base_list if num >= 0])
# negatibe_S = lambda base_list: sum([num for num in base_list if num < 0])
#
# print(positive_S(data), negatibe_S(data))

# c
# data = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# count = lambda source: {item: source.count(item) for item in source}
# print(count(data))

# task 29
# a
# data = [[1, 2, 3, 4], (0, 1, 2, 3)]
# changed_data = list(map(
#     lambda element: tuple(map(lambda num: str(num), element))
#     if type(element) == tuple
#     else list(map(lambda num: str(num), element)),data
#     ))
# print(changed_data)

# b
# data = [rn.randint(1, 50) for i in range(10)]
# digit = rn.randint(30, 40)
# filtered_data = sorted(filter(lambda num: num < digit, data))
# product = reduce(lambda x, y: x*y, filtered_data, 1)
# print(f'initial list: {data}')
# print(f'the digit: {digit}')
# print(f'filtered list: {filtered_data}')
# print(f'product: {product}')

# task 30

# a
# def logErrors(func):
#     def wrapper(*args, **kwargs):
#         try:
#             original_output = func(*args)
#         except Exception as ex:
#             print('ERROR OCCCURED')
#             print(f"Your're having problems with {ex}")
#             raise
#
#     return wrapper
#
#
# @logErrors
# def showFile(filename):
#     with open(filename, 'r') as file:
#         return file.readlines()
#
#
# print(showFile('text1.txt'))

# b
# def add_defaults(default_fields):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             c = default_fields.copy()
#             c.update(kwargs)
#             return func(*args, **c)
#
#         return wrapper
#
#     return decorator
#
#
# @add_defaults({'x': 10, 'y': 15})
# def show_fields(x, y):
#     print('x= ', x)
#     print('y= ', y)
#
#
# show_fields()
# print('---')
# show_fields(y=255)

# task 31

# a [Реализовать функцию-генератор, которая создает все возможные варианты расположения заданных элементов в матрице.]
# n = rn.randint(2, 3)
# m = rn.randint(2, 3)
# matrix = [rn.randint(1, 15) for i in range(n * m)]
# print('n: ', n)
# print('m: ', m)
# print('matrix: ', matrix)
# print('---')
#
#
# def generate(matriX):
#     for x in itertools.permutations(matriX, len(matrix)):
#         yield x
#
#
# generator = generate(matrix)
# for el in generator:
#     print(el)
#     print('**')

# b [Реализовать функцию-генератор, которая создает все возможные варианты расположения элементов на странице сайта.]
# elements = [{'id': rn.randint(100, 999)} for i in range(5)]
#
#
# def generate(data):
#     for x in itertools.permutations(data, len(data)):
#         yield x
#
#
# variants = generate(elements)
# for el in variants:
#     print(el)

# c [Создать список всех чисел Фибоначчи в заданном диапазоне, используя выражение-генератор.]
# def fibonacci_generator(maxV):
#     a, b = 0, 1
#     while a <= maxV:
#         yield a
#         a, b = b, a + b
#
#
# max_value = rn.randint(8, 400)
#
# fibonacci_list = [fib for fib in fibonacci_generator(max_value)]
#
# print('Edge value:', max_value)
# print(fibonacci_list)

# d [Отфильтровать список чисел, оставив только те, которые являются простыми числами Фибоначчи,
#                                                                                       используя выражение-генератор.]
# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# def fibonacci_generator(maxV):
#     a, b = 0, 1
#     while a <= maxV:
#         yield a
#         a, b = b, a + b
#
#
# max_value = rn.randint(8, 400)
#
# fibonacci_list = [fib for fib in fibonacci_generator(max_value) if is_prime(fib)]
#
# print(fibonacci_list)

# task 32

# a [Дан массив  𝐴  размера  𝑁 . Сформировать новый массив B того же размера по следующему правилу:
#                                                   элемент BK равен сумме элементов массива  𝐴  с номерами от 1 до  𝐾 .
# n = rn.randint(2, 10)
# a = array.array('i', [rn.randint(1, 100) for i in range(n)])
# b = array.array('i', [sum(a[0:i + 1]) for i in range(n)])
# print('n: ', n)
# print('a: ', a)
# print('b: ', b)
# print('---')

# b [Дана матрица размера  𝑀×𝑁 . Элемент матрицы называется ее локальным минимумом,
#                если он меньше всех окружающих его элементов. Заменить все локальные минимумы данной матрицы на нули.]
# n = rn.randint(5, 5)
# m = n
# matrix = np.random.randint(1, 10, size=(m, n))
# print('n: ', n)
# print('m: ', m)
# print('matrix: ', matrix, sep='\n')
# print('---')
#
#
# def replace_local_min(mat):
#     modified_matrix = mat.copy()
#
#     rows, cols = mat.shape
#
#     for i in range(1, rows - 1):
#         for j in range(1, cols - 1):
#             neighborhood = mat[i - 1:i + 2, j - 1:j + 2]
#             print('EL:', mat[i, j], 'N:', neighborhood)
#
#             if mat[i, j] == np.min(neighborhood):
#                 # print('min:', np.min(neighborhood), '\n')
#                 modified_matrix[i, j] = 0
#
#     return modified_matrix
#
#
# newM = replace_local_min(matrix)
#
# print('modified matrix:')
# print(newM)
