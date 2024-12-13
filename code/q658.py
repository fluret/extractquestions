words = ["apple", "banana", "cherry", "date"]
prefix = "ba"
words_with_prefix = {word for word in words if word.startswith(prefix)}
print(words)
print(prefix)
print(words_with_prefix)