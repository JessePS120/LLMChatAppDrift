def compare_one(a, b):
    x = float(str(a).replace(',', '.'))
    y = float(str(b).replace(',', '.'))
    return a if x > y else (b if y > x else None)