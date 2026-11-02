def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                return False
        return True
    primes = [p for p in range(2, 100) if is_prime(p)]
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False