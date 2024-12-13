words = ["apple", "banana", "cherry", "date"]
distinct_vowels = tuple(char.lower() for word in words for char in word if char.lower() in 'aeiou')
print(words)
print(distinct_vowels)