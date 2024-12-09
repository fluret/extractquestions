def check(x):
    cnt = 6 <= len(x) and len(x) <= 12
    for i in x:
        if i.isupper():
            cnt += 1
            break
    for i in x:
        if i.islower():
            cnt += 1
            break
    for i in x:
        if i.isnumeric():
            cnt += 1
            break
    for i in x:
        if i == "@" or i == "#" or i == "$":
            cnt += 1
            break
    return cnt == 5


# counting if total 5 all conditions are fulfilled then returns True


s = input().split(",")
lst = filter(check, s)
# Filter function pick the words from s, those returns True by check() function
print(",".join(lst))
