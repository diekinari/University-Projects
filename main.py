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
def RemoveRows(matrix, k1, k2):
    end = k2
    if k1 < len(matrix):
        return
    elif k2 > len(matrix):
        end = len(matrix)
    for x in range(k1, end + 1):
        matrix.remove(matrix.index(x))



m = [[1, 2, 3], [3, 2, 1], [5, 6, 7], [7, 8, 9]]
RemoveRows(m, 1, 3)
print(m)
