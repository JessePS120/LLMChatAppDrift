def generate_integers(a, b):
    return [i for i in range(min(a, b), max(a, b) + 1) if i < 10 and i % 2 == 0]