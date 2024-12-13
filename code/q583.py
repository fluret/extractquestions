sentence = "Hello, how are you?"
vowel_count_tuples = tuple((word, sum(1 for char in word if char.lower() in 'aeiou')) for word in sentence.split())
print(sentence)
print(vowel_count_tuples)