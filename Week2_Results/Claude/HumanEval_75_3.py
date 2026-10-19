def is_multiply_prime(a):
    count = 0
    factor = 2
    
    while factor * factor <= a:
        while a % factor == 0:
            count += 1
            a //= factor
        factor += 1
    
    if a > 1:
        count += 1
    
    return count == 3