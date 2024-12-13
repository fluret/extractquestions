words = ["apple", "banana", "cherry"]
sorted_descending = {''.join(sorted(word, reverse=True)) for word in words}
print(words)
print(sorted_descending)