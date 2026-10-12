def generate_integers(a, b):
    return [d for d in [0, 2, 4, 6, 8] if min(a, b) <= d <= max(a, b)]