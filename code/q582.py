words = ["apple", "banana", "cherry", "date"]
vowels = tuple(char for word in words for char in word if char.lower() in 'aeiou')
consonants = tuple(char for word in words for char in word if char.lower() not in 'aeiou')
print(words)
print(vowels)
print(consonants)