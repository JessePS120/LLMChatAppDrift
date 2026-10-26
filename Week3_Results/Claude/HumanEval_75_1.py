def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_factors = []
    divisor = 2
    temp = a
    
    while divisor * divisor <= temp:
        while temp % divisor == 0:
            prime_factors.append(divisor)
            temp //= divisor
        divisor += 1
    
    if temp > 1:
        prime_factors.append(temp)
    
    return len(prime_factors) == 3