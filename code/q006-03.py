from math import sqrt

C, H = 50, 30


def calc(D):
    return sqrt((2 * C * D) / H)


print(",".join([str(int(calc(int(i)))) for i in input().split(",")]))
