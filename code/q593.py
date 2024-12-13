sentence = "This is a sample sentence with words of various lengths."
long_word_tuples = tuple(word for word in sentence.split() if len(word) > 4)
print(sentence)
print(long_word_tuples)