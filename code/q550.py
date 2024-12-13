numbers = [1, 2, 2, 3, 4, 4, 4, 5]
element_frequencies = {num: numbers.count(num) for num in set(numbers)}
print(numbers)
print(element_frequencies)