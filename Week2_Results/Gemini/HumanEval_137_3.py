def compare_one(a, b):
    def to_num(x):
        return float(x.replace(',', '.')) if isinstance(x, str) else float(x)
    fa, fb = to_num(a), to_num(b)
    if fa > fb:
        return a
    elif fb > fa:
        return b
    return None