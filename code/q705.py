sentence = "Hello, how are you?"
word_contains_e = {word: word.count('e') for word in sentence.split()}
print(sentence)
print(word_contains_e)