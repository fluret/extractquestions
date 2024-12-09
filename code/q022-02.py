ss = input().split()
dict = {i: ss.count(i) for i in ss}
# sets dictionary as i-> split word & ss.count(i) -> total occurrence of i in ss
dict = sorted(dict.items())
# items() function returns both key & value of dictionary as a list
# and then sorted. The sort by default occurs in order of 1st -> 2nd key
for i in dict:
    print(f"{i[0]}:{i[1]}")
