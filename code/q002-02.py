n = int(input())  # input() function takes input as string type
# int() converts it to integer type
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)


def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


print(factorial(8))
