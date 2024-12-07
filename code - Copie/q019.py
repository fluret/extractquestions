from operator import itemgetter

result = []
while True:
    s = input()
    if not s:
        break
    result.append(tuple(s.split(",")))

print(sorted(result, key=itemgetter(0, 1, 2)))
