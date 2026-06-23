def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    if n > 1:
        factors.append(n)

    return factors
print(prime_factors(56))
# Временная сложност O(√n)
# Сложность по памяти  O(log n)