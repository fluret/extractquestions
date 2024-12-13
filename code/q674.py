numbers = [1, 2, 3, 4, 5]
factors = {x: [i for i in range(1, x + 1) if x % i == 0] for x in numbers}
print(numbers)
print(factors)