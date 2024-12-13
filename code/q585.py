sentence = "Hello, how are you?"
vowel_words = tuple(word for word in sentence.split() if any(char.lower() in 'aeiou' for char in word))
print(sentence)
print(vowel_words)