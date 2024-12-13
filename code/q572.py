sentence = "This is a sample sentence"
long_words = tuple(word for word in sentence.split() if len(word) > 3)
print(sentence)
print(long_words)