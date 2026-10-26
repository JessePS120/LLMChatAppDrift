def is_multiply_prime(a):
    primes = []
    d = 2
    while d * d <= a:
        while (a % d) == 0:
            primes.append(d)
            a //= d
        d += 1
    if a > 1:
        primes.append(a)
    return len(primes) == 3