def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = [p for p in range(2, a + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False