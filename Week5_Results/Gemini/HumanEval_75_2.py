def is_multiply_prime(a):
    c = 0
    d = 2
    while d <= a:
        while a % d == 0:
            c += 1
            a //= d
        d += 1
    return c == 3