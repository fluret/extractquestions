sentence = "Hello, how are you?"
vowels = tuple(char for char in sentence if char.lower() in 'aeiou')
print(sentence)
print(vowels)