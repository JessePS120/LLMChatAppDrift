def compare_one(a, b):
    def parse(x):
        return float(x.replace(',', '.')) if isinstance(x, str) else float(x)
    fa, fb = parse(a), parse(b)
    if fa == fb:
        return None
    return a if fa > fb else b