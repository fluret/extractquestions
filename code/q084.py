def digits_sum(num):
    aux = 0
    for x in str(num):
        aux = aux + int(x)
    return aux


# Invoke the function with any three-digit number
print(digits_sum(123))
