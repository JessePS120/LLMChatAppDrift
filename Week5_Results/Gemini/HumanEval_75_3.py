def is_multiply_prime(a):
    count = 0
    d = 2
    while d * d <= a:
        while a % d == 0:
            count += 1
            a //= d
        d += 1
    if a > 1:
        count += 1
    return count == 3