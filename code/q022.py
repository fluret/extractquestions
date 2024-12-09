ss = input().split()
word = sorted(set(ss))
# split words are stored and sorted as a set

for i in word:
    print("{0}:{1}".format(i, ss.count(i)))
