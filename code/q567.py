sentence = "Hello, how are you?"
consonants = tuple(char.lower() for char in sentence if char.lower() not in 'aeiou' and char.isalpha())
print(sentence)
print(consonants)