words = ["apple", "banana", "cherry", "date"]
swapped_words = [word[-1] + word[1:-1] + word[0] for word in words]
print(words)
print(swapped_words)