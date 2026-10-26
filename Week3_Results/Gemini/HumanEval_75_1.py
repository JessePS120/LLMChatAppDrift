def is_multiply_prime(a):
    factors = []
    d = 2
    temp = a
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return len(factors) == 3