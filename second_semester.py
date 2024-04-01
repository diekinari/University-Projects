import itertools
import math
import datetime
import random as rn
import numpy as np
import array
from icecream import ic
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
# task 33
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[len(self.items) - 1]
#
#     def size(self):
#         return len(self.items)
#
#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#
#
# class Stack2:
#     def __init__(self):
#         self.top = None
#         self.size = 0
#
#     def push(self, item):
#         new_node = Node(item)
#         if self.top is None:
#             self.top = new_node
#         else:
#             new_node.next = self.top
#             self.top = new_node
#         self.size += 1
#
#     def pop(self):
#         if self.top is None:
#             return None
#         else:
#             popped_item = self.top.data
#             self.top = self.top.next
#             self.size -= 1
#             return popped_item
#
#     def peek(self):
#         if self.top is None:
#             return None
#         return self.top.data
#
#     def is_empty(self):
#         return self.size == 0
#
#     def size(self):
#         return self.size
#
#
# s = Stack2()
# word = 'топот'
# for letter in word:
#     s.push(letter)
#
# reversed_word = ''
# while not s.is_empty():
#     reversed_word += s.pop()
#
# print(reversed_word == word)

# task 34
# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def enqueue(self, item):
#         self.items.append(item)
#
#     def peek(self):
#         return self.items[0]
#
#     def dequeue(self):
#         return self.items.pop(0)
#
#     def size(self):
#         return len(self.items)
#
#
# class QueueL:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.size = 0
#
#     def is_empty(self):
#         return self.size == 0
#
#     def enqueue(self, item):
#         new_node = Node(item)
#         if self.is_empty():
#             self.front = new_node
#             self.rear = new_node
#             self.front.next = self.rear
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
#         self.size += 1
#
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         else:
#             item = self.front.data
#             self.front = self.front.next
#             self.size -= 1
#             if self.is_empty():
#                 self.rear = None
#             return item
#
#     def peek(self):
#         if self.is_empty():
#             return None
#         else:
#             return self.front.data
#
#     def size(self):
#         return self.size
#
#
# # Создать класс двусторонней очереди, который будет поддерживать операции добавления элемента в начало и конец очереди,
# # удаления элемента из начала и конца очереди, а также удаления минимального и максимального элементов из очереди.
# # class TwoSidedNode(Node):
# #     def __init__(self, data):
# #         super().__init__(data)
# #         self.next = None
# #         self.prev = None
#
#
# # class TwoSidedQueue:
# #     def __init__(self):
# #         self.front = None
# #         self.rear = None
# #         self.size = 0
# #
# #     def is_empty(self):
# #         return self.size == 0
# #
# #     def enqueue(self, item):  # adding to an end
# #         new_node = TwoSidedNode(item)
# #         if self.is_empty():
# #             self.front = new_node
# #             self.rear = new_node
# #             self.front.prev = self.rear
# #             self.rear.next = self.front
# #         else:
# #             self.rear.prev = new_node
# #             new_node.front = self.rear
# #             self.rear = new_node
# #         self.size += 1
# #
# #     def startEnqueue(self, item):  # adding to the beginning
# #         new_node = TwoSidedNode(item)
# #         if self.is_empty():
# #             self.front = new_node
# #             self.rear = new_node
# #             self.front.prev = self.rear
# #             self.rear.next = self.front
# #         else:
# #             self.front.next = new_node
# #             new_node.prev = self.front
# #             self.front = new_node
# #         self.size += 1
# #
# #     def dequeue(self):  # deleting from the beginning
# #         if self.is_empty():
# #             return None
# #         else:
# #             item = self.front.data
# #             if self.front.prev is not None:
# #                 self.front.prev.next = None
# #             self.front = self.front.prev
# #             self.size -= 1
# #             if self.is_empty():
# #                 self.rear = None
# #             return item
# #
# #     def endDequeue(self):  # deleting from the end
# #         if self.is_empty():
# #             return None
# #         else:
# #             item = self.rear.data
# #             self.rear = self.rear.next
# #
# #             self.size -= 1
# #             if self.is_empty():
# #                 self.front = None
# #             return item
# #
# #     def peek(self):
# #         if self.is_empty():
# #             return None
# #         else:
# #             return self.front.data
# #
# #     def size(self):
# #         return self.size
#
# # t_q = TwoSidedQueue()
# # # add to end
# # t_q.enqueue(1)
# # t_q.enqueue(2)
# # t_q.enqueue(3)
# # t_q.enqueue(4)
# # t_q.enqueue(5)
# # ic(t_q.peek())
# #
# # # delete 1 at start
# # ic(t_q.dequeue())
# # # add 10 to start
# # t_q.startEnqueue(10)
# # ic(t_q.peek())
# # # delete 10
# # t_q.dequeue()
# # # show next start
# # ic(t_q.peek())
# #
# # # delete 5 at end
# # ic(t_q.endDequeue())
#
# class DoubleEndedQueue:
#     def __init__(self):
#         self.queue = []
#
#     def add_front(self, item):
#         self.queue.insert(0, item)
#
#     def add_rear(self, item):
#         self.queue.append(item)
#
#     def remove_front(self):
#         if self.is_empty():
#             return None
#         return self.queue.pop(0)
#
#     def remove_rear(self):
#         if self.is_empty():
#             return None
#         return self.queue.pop()
#
#     def remove_min(self):
#         if self.is_empty():
#             return None
#         min_val = min(self.queue)
#         self.queue.remove(min_val)
#         return min_val
#
#     def remove_max(self):
#         if self.is_empty():
#             return None
#         max_val = max(self.queue)
#         self.queue.remove(max_val)
#         return max_val
#
#     def is_empty(self):
#         return len(self.queue) == 0
#
#     def size(self):
#         return len(self.queue)
#
#
# deque = DoubleEndedQueue()
# deque.add_front(10)
# deque.add_rear(20)
# deque.add_front(5)
#
# print("Size of deque:", deque.size())
# print("Removed from front:", deque.remove_front())
# print("Removed from rear:", deque.remove_rear())
# print("Size of deque after removals:", deque.size())
#
# deque.add_rear(30)
# deque.add_front(2)
# deque.add_rear(25)
#
# print("Deque:", deque.queue)
# print("Removed min value:", deque.remove_min())
# print("Removed max value:", deque.remove_max())
# print("Deque after min and max removals:", deque.queue)

# task 35
# Создайте двусвязный список для хранения информации о задачах в проекте по разработке программного обеспечения.
# Каждый элемент списка должен содержать название задачи, описание, дату начала и дату окончания, а также информацию о
# том, какие разработчики работают над этой задачей.
class DevelopingTask:
    def __init__(self, title, description, startDate, endDate, developersList):
        self.title = title
        self.description = description
        self.startDate = startDate
        self.endDate = endDate
        self.developersList = developersList

    def __str__(self):
        return f'{self.title}, {self.description}, {self.startDate}, {self.endDate}, {self.developersList}'


class TwoSidedNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.next = None
        self.prev = None


class TwoSidedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_end(self, item):  # adding to an end
        new_node = TwoSidedNode(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.front.prev = self.rear
            self.rear.next = self.front
        else:
            self.rear.prev = new_node
            new_node.next = self.rear
            self.rear = new_node
        self.size += 1

    def add_start(self, item):  # adding to the beginning
        new_node = TwoSidedNode(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.front.prev = self.rear
            self.rear.next = self.front
        else:
            self.front.next = new_node
            new_node.prev = self.front
            self.front = new_node
        self.size += 1

    def del_start(self):  # deleting from the beginning
        if self.is_empty():
            return None
        else:
            item = self.front.data
            if self.front.prev is not None:
                self.front.prev.next = None
            self.front = self.front.prev
            self.size -= 1
            if self.is_empty():
                self.rear = None
            return item

    def del_end(self):  # deleting from the end
        if self.is_empty():
            return None
        else:
            item = self.rear.data
            if self.rear.next is not None:
                self.rear.next.prev = None
            self.rear = self.rear.next
            self.size -= 1
            if self.is_empty():
                self.front = None
            return item

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.front.data

    def size(self):
        return self.size


#
# tq = TwoSidedList()
# tq.add_end(DevelopingTask('website', 'desc1', '01-03-24', '05-03-24', ['Mark', 'John']))
# tq.add_end(DevelopingTask('server side', 'desc2', '20-03-24', '30-03-24', ['Mark', 'Alex']))
# print(tq.size)
# print(tq.peek())

# task 36
# def find_intersection(l1, l2):
#     visited = {}
#     current = l1.rear
#
#     for i in range(l1.size):
#         visited[current.data] = True
#         current = current.next
#
#     current = l2.rear
#     for i in range(l2.size):
#
#         if current.data in visited:
#             return current.data
#         current = current.next
#
#     return None
#
#
# list1 = TwoSidedList()
# list1.add_end(1)
# list1.add_end(2)
# list1.add_end(3)
# list1.add_end(4)
#
# list2 = TwoSidedList()
# list2.add_end(4)
# list2.add_end(5)
# list2.add_end(6)
# list2.add_end(7)
#
# print(find_intersection(list1, list2))

# task 37
# class CycleTwoSidedList:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.size = 0
#
#     def is_empty(self):
#         return self.size == 0
#
#     def add_end(self, item):  # adding to an end
#         new_node = TwoSidedNode(item)
#         if self.is_empty():
#             self.front = new_node
#             self.rear = new_node
#             self.front.prev = self.rear
#             self.front.next = self.rear
#             self.rear.next = self.front
#             self.rear.prev = self.front
#         else:
#             self.front.next = new_node
#             self.rear.prev = new_node
#             new_node.next = self.rear
#             new_node.prev = self.front
#             self.rear = new_node
#         self.size += 1
#
#     def add_start(self, item):  # adding to the beginning
#         new_node = TwoSidedNode(item)
#         if self.is_empty():
#             self.front = new_node
#             self.rear = new_node
#             self.front.prev = self.rear
#             self.front.next = self.rear
#             self.rear.next = self.front
#             self.rear.prev = self.front
#         else:
#             self.rear.prev = new_node
#             self.front.next = new_node
#             new_node.prev = self.front
#             new_node.next = self.rear
#             self.front = new_node
#         self.size += 1
#
#     def add_at_position(self, item, position):
#         position -= 1
#         if position < 0 or position > self.size:
#             raise IndexError("Invalid position")
#         if position == 0:
#             self.add_start(item)
#         elif position == self.size:
#             self.add_end(item)
#         else:
#             new_node = TwoSidedNode(item)
#             current = self.front
#             for i in range(position):
#                 current = current.prev
#             new_node.next = current.next
#             new_node.prev = current
#             current.next.prev = new_node
#             current.next = new_node
#             self.size += 1
#
#     def del_start(self):  # deleting from the beginning
#         if self.is_empty():
#             return None
#         else:
#             item = self.front.data
#             if self.front.prev is not None:
#                 self.front.prev.next = self.rear
#             self.front = self.front.prev
#             self.size -= 1
#             if self.is_empty():
#                 self.rear = None
#             return item
#
#     def del_end(self):  # deleting from the end
#         if self.is_empty():
#             return None
#         else:
#             item = self.rear.data
#             if self.rear.next is not None:
#                 self.rear.next.prev = self.front
#             self.rear = self.rear.next
#             self.size -= 1
#             if self.is_empty():
#                 self.front = None
#             return item
#
#     def peek(self):
#         if self.is_empty():
#             return None
#         else:
#             return self.front.data
#
#     def size(self):
#         return self.size
#
#
# list1 = CycleTwoSidedList()
# list1.add_end(1)
# list1.add_end(2)
# list1.add_end(3)
# list1.add_end(4)
# list1.add_at_position(999, 2)
# print(list1.front.data, list1.front.prev.data)

# task 38
# Необходимо отсортировать массив объектов по определенному полю и вывести результат на экран. В зависимости от
# переданного параметра отсортировать массив объектов по возрастанию или по убыванию значения определенного поля,
# используя алгоритмы сортировки: сортировку выбором, сортировку пузырьком и быструю сортировку.
# Сравнить время выполнения алгоритмов сортировки с помощью декоратора. Данные об объектах хранятся в файле.


