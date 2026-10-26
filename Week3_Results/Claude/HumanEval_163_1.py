def generate_integers(a, b):
    min_val = min(a, b)
    max_val = max(a, b)
    even_digits = [0, 2, 4, 6, 8]
    return [digit for digit in even_digits if min_val <= digit <= max_val]