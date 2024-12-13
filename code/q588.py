word = "hello"
substrings = tuple(word[i:j+1] for i in range(len(word)) for j in range(i, len(word)))
print(word)
print(substrings)