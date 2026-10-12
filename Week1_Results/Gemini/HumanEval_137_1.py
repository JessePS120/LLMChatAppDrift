def compare_one(a, b):
    def parse(x):
        return float(str(x).replace(',', '.'))
    fa = parse(a)
    fb = parse(b)
    if fa == fb:
        return None
    return b if fb > fa else a