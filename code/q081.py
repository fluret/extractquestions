def swap_digits(num):
    aux = str(num)[1] + str(num)[0]
    return int(aux)


# Invoke the function with any two-digit integer as its argument
print(swap_digits(79))
