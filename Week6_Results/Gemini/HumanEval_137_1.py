def compare_one(a, b):
    fa = float(a.replace(',', '.')) if isinstance(a, str) else float(a)
    fb = float(b.replace(',', '.')) if isinstance(b, str) else float(b)
    if fa == fb:
        return None
    return b if fb > fa else a