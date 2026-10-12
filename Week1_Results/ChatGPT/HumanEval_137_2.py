def compare_one(a, b):
    x = float(str(a).replace(",", "."))
    y = float(str(b).replace(",", "."))
    if x == y:
        return None
    return a if x > y else b