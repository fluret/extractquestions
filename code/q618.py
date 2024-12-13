string = "Hello, world!"
non_vowels = {char for char in string if char.lower() not in 'aeiou'}
print(string)
print(non_vowels)