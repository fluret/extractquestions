sentence = "madam sees the racecar"
word_is_palindrome = {word: word == word[::-1] for word in sentence.split()}
print(sentence)
print(word_is_palindrome)