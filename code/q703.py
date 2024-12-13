import string
 
sentence = "Hello, how are you?"
char_occurrence_no_punct = {char: sentence.count(char) for char in set(sentence) if char not in string.punctuation}
print(sentence)
print(char_occurrence_no_punct)