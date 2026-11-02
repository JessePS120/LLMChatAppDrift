def is_multiply_prime(a):
    primes = [p for p in range(2, 100) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False