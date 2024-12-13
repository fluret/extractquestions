words = ['apple', 'banana', 'cherry']
without_vowels = {word: ''.join([char for char in word if char.lower() not in 'aeiou']) for word in words}
print(words)
print(without_vowels)