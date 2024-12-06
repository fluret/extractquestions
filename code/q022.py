freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = list(freq.keys())
words.sort()
print()
for w in words:
    print(f"{w}:{freq[w]}")