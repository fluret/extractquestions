string = "Hello, world!"
consonants = {char for char in string if char.isalpha() and char.lower() not in 'aeiou'}
print(string)
print(consonants)