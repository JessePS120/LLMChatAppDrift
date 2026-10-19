def is_multiply_prime(a):
    factors = []
    d = 2
    n = a
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return len(factors) == 3