word1 = "apple"
word2 = "cherry"
common_letter_tuples = tuple((char, char) for char in word1 if char in word2)
print(word1)
print(word2)
print(common_letter_tuples)