def compare_one(a, b):
    val_a = float(str(a).replace(',', '.'))
    val_b = float(str(b).replace(',', '.'))
    if val_a > val_b:
        return a
    elif val_b > val_a:
        return b
    return None