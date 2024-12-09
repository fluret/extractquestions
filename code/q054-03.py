def question_62(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    sequence = [0, 1]
    a, b = 0, 1
    for x in range(2, n + 1):
        c = a + b
        sequence.append(c)
        a = b
        b = c
    return sequence


print(question_62(10))
