def generate_integers(a, b):
    return [i for i in range(min(a, b), min(max(a, b), 9) + 1) if i % 2 == 0]