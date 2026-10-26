def generate_integers(a, b):
    if a > b:
        a, b = b, a
    
    even_digits = [0, 2, 4, 6, 8]
    return [digit for digit in even_digits if a <= digit <= b]