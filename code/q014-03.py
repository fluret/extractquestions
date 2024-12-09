word = input()
upper = sum(1 for i in word if i.isupper())
# sum function cumulatively sum up 1's if the condition is True
lower = sum(1 for i in word if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))
