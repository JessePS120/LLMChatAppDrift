def generate_integers(a, b):
    start, end = sorted((a, b))
    return [n for n in range(start, end + 1) if n % 2 == 0 and n < 10]