num = int(input())
scores = list(map(int, input().split(' ')))
winner = max(scores)
lst = []

if len(scores) != num:
    print('length of score is greater than input given')
else:
    for score in scores:
        if winner > score:
            lst.append(score)

runnerup = max(lst)
print(runnerup)