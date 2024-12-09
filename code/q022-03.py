from collections import Counter

ss = input().split()
ss = Counter(ss)
# returns key & frequency as a dictionary
ss = sorted(ss.items())
# returns as a tuple list

for i in ss:
    print("%s:%d" % (i[0], i[1]))
