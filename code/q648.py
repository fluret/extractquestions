strings = ["apple", "banana", "cherry"]
capitalized_strings = {' '.join([word.capitalize() for word in string.split()]) for string in strings}
print(strings)
print(capitalized_strings)