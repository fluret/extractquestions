numbers = [-2, 3, -5, 7, -11]
num_signs = [(x, 'positive') if x > 0 else (x, 'negative') for x in numbers]
print(numbers)
print(num_signs)