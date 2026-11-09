def compare_one(a, b):
    def parse(x):
        if isinstance(x, str):
            return float(x.replace(",", "."))
        return float(x)
    va, vb = parse(a), parse(b)
    if va == vb:
        return None
    return a if va > vb else b