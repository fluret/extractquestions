words = ["apple", "banana", "cherry"]
unique_vowels = {char for word in words for char in word if char.lower() in 'aeiou'}
print(words)
print(unique_vowels)