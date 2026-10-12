def is_multiply_prime(a):
    count = 0
    for i in range(2, a + 1):
        while a % i == 0:
            is_prime = all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))
            if not is_prime:
                break
            count += 1
            a //= i
        if a == 1:
            break
    return count == 3 and a == 1