words = ["apple", "banana", "cherry", ]
vowel_words = {word for word in words if any(char.lower() in 'aeiou' for char in word)}
print(words)
print(vowel_words)