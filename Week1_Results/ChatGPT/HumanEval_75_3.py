def is_multiply_prime(a):
    count = 0
    for i in range(2, a + 1):
        while a % i == 0:
            if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
                count += 1
                a //= i
            else:
                break
    return count == 3 and a == 1