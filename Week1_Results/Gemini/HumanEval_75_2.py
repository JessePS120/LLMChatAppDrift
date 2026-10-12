def is_multiply_prime(a):
    c = 0
    d = 2
    temp = a
    while d * d <= temp:
        while temp % d == 0:
            c += 1
            temp //= d
        d += 1
    if temp > 1:
        c += 1
    return c == 3