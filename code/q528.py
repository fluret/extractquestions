def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 
prime_sum_pairs = [(x, y) for x in range(1, 11) for y in range(1, 11) if is_prime(x + y)]
 
print(prime_sum_pairs)