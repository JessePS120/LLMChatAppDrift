def generate_integers(a, b):
    low, high = min(a, b), max(a, b)
    return [n for n in range(low, high + 1) if n < 10 and n % 2 == 0]