def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
 
factorials = {x: factorial(x) for x in range(1, 11)}
print(factorials)