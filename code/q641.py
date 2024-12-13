strings = {"apple", "banana", "cherry"}
no_vowels = {''.join([char for char in word if char.lower() not in 'aeiou']) for word in strings}
print(strings)
print(no_vowels)