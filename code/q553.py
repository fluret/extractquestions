characters = ['a', 'b', 'c', 'e', 'f', 'i', 'o']
vowels = [char for char in characters if char.lower() in 'aeiou']
consonants = [char for char in characters if char.lower() not in 'aeiou']
print(characters)
print(vowels)
print(consonants)