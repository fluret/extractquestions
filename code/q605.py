sentence = "Hello, how are you?"
divisible_by_3_length_word_length_tuples = tuple((word, len(word)) for word in set(sentence.split()) if len(word) % 3 == 0)
 
print(sentence)
print(divisible_by_3_length_word_length_tuples)