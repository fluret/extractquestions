words = {"apple", "banana", "cherry"}
vowel_replaced = {''.join(['_' if char.lower() in 'aeiou' else char for char in word]) for word in words}
print(words)
print(vowel_replaced)