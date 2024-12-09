phrase = input().split()
ans = []
for word in phrase:
    if word.isdigit():     # can also use isnumeric() / isdecimal() function instead
        ans.append(word)
print(ans)