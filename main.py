# task 11 v 8
# a)
# d1 = {x: x*2 for x in range(1, 6)}
# d2 = {x: x*2 for x in range(6, 11)}
# d1.update(d2.items())
# print(d1)

# b)
# d1 = {x: x*2 for x in range(1, 6)}
# for el in d1.items():
#     print(*el, sep=': ')

# c)
# l1 = ['key1','data2','data3']
# l2 = ['key2', 'pass2', 'pass3']
# d1 = dict()
# for i in [l1, l2]:
#     temp_d = {i[0]: i[1:3]}
#     d1.update(temp_d)
# print(d1)

# task 12
# a)
# login = input('Login: ')
# password = input('Password: ')
# k = ({'log': login}, {'pass': password})
# print(k)

# b)
# k = (1.24, 133, 85, 0, 3.5)
# temp_l = [x for x in k if type(x) == float]
# temp_l2 = [y for y in k if y not in temp_l]
# temp_l.sort()
# temp_l2.sort()
# fL = (*temp_l, *temp_l2)
# print(fL)

# task 13
# s1 = 'red'
# s2 = 'fox'
# s3 = ['redfox', 'red fox', 'reddfox']
# for i in range(3):
#     if len(set(s1)) + len(set(s2)) == len(set(s3[i])):
#         if len(set(s3[i])) != len(s3[i]):
#             repeated_symbol = ''
#             for l in s3[i]:
#                 if s3[i].count(l) > 1:
#                     repeated_symbol = l
#                     break
#             if (s1 + s2).count(repeated_symbol) == s3[i].count(repeated_symbol):
#                 print(True)
#             else:
#                 print(False)
#         else:
#             print(True)
#     else:
#         print(False)