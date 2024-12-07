import math


def car_route(n, m):
    return int(math.ceil(m / n))


# Invoke the function with two integers
print(car_route(35, 50))
