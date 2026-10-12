def compare_one(a, b):
    x = float(a.replace(",", ".") if isinstance(a, str) else a)
    y = float(b.replace(",", ".") if isinstance(b, str) else b)
    if x == y:
        return None
    return a if x > y else b