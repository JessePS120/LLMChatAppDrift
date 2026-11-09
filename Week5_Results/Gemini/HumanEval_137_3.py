def compare_one(a, b):
    fa = float(a.replace(',', '.')) if isinstance(a, str) else float(a)
    fb = float(b.replace(',', '.')) if isinstance(b, str) else float(b)
    if fa == fb:
        return None
    return a if fa > fb else b