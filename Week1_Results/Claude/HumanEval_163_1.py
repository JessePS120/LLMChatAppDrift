def generate_integers(a, b):
    if a > b:
        a, b = b, a
    
    result = []
    for digit in [0, 2, 4, 6, 8]:
        if a <= digit <= b:
            result.append(digit)
    
    return result