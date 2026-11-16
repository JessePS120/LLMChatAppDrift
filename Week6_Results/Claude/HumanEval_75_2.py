def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    n = a
    for p in range(2, a + 1):
        while is_prime(p) and n % p == 0:
            n //= p
            count += 1
    return count == 3 and n == 1