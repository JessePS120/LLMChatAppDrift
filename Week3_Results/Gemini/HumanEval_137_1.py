def compare_one(a, b):
    def parse(x):
        if isinstance(x, (int, float)):
            return float(x)
        return float(str(x).replace(',', '.'))
    va, vb = parse(a), parse(b)
    if va > vb:
        return a
    if vb > va:
        return b
    return None