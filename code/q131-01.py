X = input()
my_set = set(X)
arr = []
for item in my_set:
    arr.append([item, X.count(item)])
tmp = sorted(arr, key=lambda x: (-x[1], x[0]))

for i in tmp:
    print(i[0] + " " + str(i[1]))
