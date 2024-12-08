import math


def first_digit(num):
    return int(str(math.floor(num * 10) / 10)[-1])


def first_digit2(num):
    result = str(num).split(".")
    return int(result[1][0])


# Invoke the function with a positive real number. ex. 34.33
print(first_digit(2.6))
print(first_digit(1.79))
print(first_digit2(4.2))
print(first_digit2(3.14))
