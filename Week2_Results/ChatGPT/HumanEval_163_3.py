def generate_integers(a, b):
    return [n for n in range(min(a, b), max(a, b) + 1) if n % 2 == 0 and n < 10]