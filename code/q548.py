sentence = "This is a sample sentence with some vowels."
no_vowels = [''.join([char for char in word if char.lower() not in 'aeiou']) for word in sentence.split()]
print(sentence)
print(no_vowels)