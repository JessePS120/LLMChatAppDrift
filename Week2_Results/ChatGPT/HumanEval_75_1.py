def is_multiply_prime(a):
    count = 0
    for i in range(2, a + 1):
        while a % i == 0:
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
                a //= i
            else:
                break
        if count > 3:
            return False
    return count == 3 and a == 1