sentence = "Python is fun"
reversed_words = {i: word for i, word in enumerate(sentence.split()[::-1])}
print(sentence)
print(reversed_words)