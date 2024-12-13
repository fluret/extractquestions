sentence = "This is a sample sentence with various words."
ae_words = tuple(word for word in sentence.split() if 'a' in word or 'e' in word)
print(sentence)
print(ae_words)