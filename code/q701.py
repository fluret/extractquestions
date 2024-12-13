sentence = "Hello, how are you?"
distinct_word_length_no_odd = {word: len(word) for word in set(sentence.split()) if len(word) % 2 == 0}
print(sentence)
print(distinct_word_length_no_odd)