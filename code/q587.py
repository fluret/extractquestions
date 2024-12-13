words = ["apple", "banana", "cherry", "date"]
reversed_tuples = tuple((word, word[::-1]) for word in words)
print(words)
print(reversed_tuples)