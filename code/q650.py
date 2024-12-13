words = ["apple", "banana", "cherry"]
tripled_chars = {''.join([char*3 for char in word]) for word in words}
print(words)
print(tripled_chars)