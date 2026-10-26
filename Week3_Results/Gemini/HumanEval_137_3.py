def compare_one(a, b):
    def get_val(x):
        if isinstance(x, str):
            return float(x.replace(',', '.'))
        return float(x)
    va, vb = get_val(a), get_val(b)
    if va == vb:
        return None
    return a if va > vb else b