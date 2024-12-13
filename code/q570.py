sentence = "Hello, how are you?"
vowel_start_words = tuple(word for word in sentence.split() if word[0].lower() in 'aeiou')
print(sentence)
print(vowel_start_words)