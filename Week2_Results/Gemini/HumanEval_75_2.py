def is_multiply_prime(a):
    n = a
    c = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            c += 1
            n //= d
        d += 1
    if n > 1:
        c += 1
    return c == 3