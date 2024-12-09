import itertools

subject = ["I", "You"]
verb = ["Play", "Love"]
objects = ["Hockey", "Football"]

sentence = [subject, verb, objects]
n = list(itertools.product(*sentence))
for i in n:
    print(i)
