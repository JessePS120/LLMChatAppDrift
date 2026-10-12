def generate_integers(a, b):
    low, high = min(a, b), max(a, b)
    return [i for i in range(max(0, low), min(9, high) + 1) if i % 2 == 0]