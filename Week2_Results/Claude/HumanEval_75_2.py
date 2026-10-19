def is_multiply_prime(a):
    count = 0
    
    while a % 2 == 0:
        count += 1
        a = a // 2
    
    i = 3
    while i * i <= a:
        while a % i == 0:
            count += 1
            a = a // i
        i += 2
    
    if a > 1:
        count += 1
    
    return count == 3