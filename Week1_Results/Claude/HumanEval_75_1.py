def is_multiply_prime(a):
    count = 0
    temp = a
    
    d = 2
    while d * d <= temp:
        while temp % d == 0:
            count += 1
            temp //= d
        d += 1
    
    if temp > 1:
        count += 1
    
    return count == 3