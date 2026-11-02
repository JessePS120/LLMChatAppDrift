def is_multiply_prime(a):
    count = 0
    for i in range(2, a + 1):
        while a % i == 0:
            count += 1
            a //= i
        if count > 3:
            return False
    return count == 3 and a == 1