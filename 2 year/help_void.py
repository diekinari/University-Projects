# Redefining the data and calculations due to state reset
import math


def cur_p(c, n, k):
    return (2 * (c * n + 1 - k)) / (k - 1 + n * (1 + k))



def dur(p, n, c):
    return ((1 + p) / p) - ((n * (c - p) + 1 + p) / (c * ((1 + p) ** n - 1) + p))


print((-0.15 * (100/3)) + (0.18 * (100/3))+ (0.23 * (100/3)))
# print(dur(cur_p(0.1, 5, 0.8), 5, 0.1))
# # Given data
# C = 700  # annual coupon payment
# M = 2500  # face value of the bond
# i = 0.1  # annual discount rate
# n = 5  # years to maturity
#
# # Calculating the present value of coupon payments
# coupon_pv = sum([C / (1 + i) ** t for t in range(1, n + 1)])
#
# # Calculating the present value of the face value
# face_value_pv = M / (1 + i) ** n
#
# # Total present value of the bond
# P = coupon_pv + face_value_pv
# print(P)
