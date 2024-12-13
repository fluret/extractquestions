import random
 
words = ["apple", "banana", "cherry"]
shuffled_chars = {''.join(random.sample(word, len(word))) for word in words}
print(words)
print(shuffled_chars)