def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, a):
        if not is_prime(i):
            continue
        for j in range(i, a):
            if not is_prime(j):
                continue
            for k in range(j, a):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False