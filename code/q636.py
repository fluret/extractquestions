words = ["apple", "banana", "cherry"]
duplicated_chars = {''.join([char*2 for char in word]) for word in words}
print(words)
print(duplicated_chars)