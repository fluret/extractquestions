# old school
no_dups = set()
for n in range(1, 101):
    for x in range(2, 10):
        if n % x == 0:
            no_dups.add(n)
print(no_dups)
print()

# nested list comprehension

result = [
    number
    for number in range(1, 101)
    if True in [True for x in range(2, 10) if number % x == 0]
]
print(result)


numbers = list(range(1,101))
divisors = list(range(2,10))

ans = [n for n in numbers if any([ n % d == 0 for d in divisors])]
print(ans)

print([*set([i for i in range(1,101) for j in [2,3,4,5,6,7,8,9] if i % j == 0])])




#Just to be a smart-arse, using the full range 2-10 is unnecessary, because if a number isn't divisible by 2, it won't be divisible by 4, 6, 8 etc.
#So a simplified version of this is:

result = [n for n in range(1001) if 0 in [n % divisor for divisor in [2,3,5,7]]]

