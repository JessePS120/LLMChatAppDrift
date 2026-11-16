def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, a):
        if not is_prime(i) or a % i != 0:
            continue
        for j in range(i, a):
            if not is_prime(j) or (a // i) % j != 0:
                continue
            k = a // (i * j)
            if k >= j and is_prime(k):
                return True
    return False