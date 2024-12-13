sentence = "This is a sample sentence with words starting with vowels."
vowel_start_words = {word for word in sentence.split() if word[0].lower() in 'aeiou'}
print(sentence)
print(vowel_start_words)