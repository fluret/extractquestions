words = ["apple", "banana", "elppa", "race", "care", "cherry"]
anagrams = {''.join(sorted(word)) for word in words}
print(words)
print(anagrams)