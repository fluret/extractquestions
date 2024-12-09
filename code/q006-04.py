from math import *  # importing all math functions

C, H = 50, 30


def calc(D):
    D = int(D)
    return str(int(sqrt((2 * C * D) / H)))


D = input().split(",")
D = list(map(calc, D))  # applying calc function on D and storing as a list
print(",".join(D))
