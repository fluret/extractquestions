ss = input().split()
dict = {}
for i in ss:
    i = dict.setdefault(i, ss.count(i))
    # setdefault() function takes key & value to set it as dictionary.

dict = sorted(dict.items())
# items() function returns both key & value of dictionary as a list
# and then sorted. The sort by default occurs in order of 1st -> 2nd key
for i in dict:
    print(f"{i[0]}:{i[1]}")
