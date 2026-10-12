def compare_one(a, b):
    def val(x):
        return float(x.replace(',', '.')) if isinstance(x, str) else x
    va, vb = val(a), val(b)
    if va > vb:
        return a
    if vb > va:
        return b
    return None