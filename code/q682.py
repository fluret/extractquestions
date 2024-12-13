words = ['apple', 'banana', 'cherry']
underscored_words = {word: ''.join(['_' if char.lower() in 'aeiou' else char for char in word]) for word in words}
print(words)
print(underscored_words)