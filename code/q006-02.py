from math import sqrt

C, H = 50, 30


def calc(D):
    return sqrt((2 * C * D) / H)


D = input().split(",")  # splits in comma position and set up in list
D = [
    str(round(calc(int(i)))) for i in D
]  # using comprehension method. It works in order of the previous code
print(",".join(D))
