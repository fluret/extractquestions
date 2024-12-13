sentence = "Hello, how are you?"
distinct_reversed_word_tuples = tuple((word, word[::-1]) for word in set(sentence.split()))
print(sentence)
print(distinct_reversed_word_tuples)