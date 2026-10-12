def is_multiply_prime(a):
    count = 0
    for i in range(2, a + 1):
        while a % i == 0:
            if any(i % j == 0 for j in range(2, i)):
                break
            a //= i
            count += 1
            if count > 3:
                return False
    return count == 3 and a == 1