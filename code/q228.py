fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


def is_prime(num):
    prime_check = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                prime_check = False
                break
        else:
            prime_check = True
    return prime_check


primes = [number for number in numbers if is_prime(number)]
print(primes)
