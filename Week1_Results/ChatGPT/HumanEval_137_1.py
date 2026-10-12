def compare_one(a, b):
    x = float(str(a).replace(",", "."))
    y = float(str(b).replace(",", "."))
    if x > y:
        return a
    if y > x:
        return b
    return None