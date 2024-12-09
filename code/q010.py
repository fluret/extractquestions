word = input().split()

for i in word:
    if (
        word.count(i) > 1
    ):  # count function returns total repeatation of an element that is send as argument
        word.remove(i)  # removes exactly one element per call

word.sort()
print(" ".join(word))
