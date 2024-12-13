sentence = "Python is a powerful and versatile programming language"
long_words = {word: len(word) for word in sentence.split() if len(word) > 4}
print(sentence)
print(long_words)