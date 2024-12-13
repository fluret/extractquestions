words = ['apple', 'Banana', 'cherry', 'Date']
uppercase_words = {word: word.upper() for word in words if any(char.isupper() for char in word)}
print(words)
print(uppercase_words)