def is_multiply_prime(a):
    count = 0
    divisor = 2
    
    while divisor * divisor <= a:
        while a % divisor == 0:
            count += 1
            a //= divisor
        divisor += 1
    
    if a > 1:
        count += 1
    
    return count == 3