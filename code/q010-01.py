word = input().split()
[word.remove(i) for i in word if word.count(i) > 1]  # removal operation with comprehension method
word.sort()
print(" ".join(word))
