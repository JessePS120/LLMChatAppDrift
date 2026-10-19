def is_multiply_prime(a):
    factors = []
    d = 2
    while d * d <= a:
        while (a % d) == 0:
            factors.append(d)
            a //= d
        d += 1
    if a > 1:
        factors.append(a)
    return len(factors) == 3