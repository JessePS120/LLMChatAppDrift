def compare_one(a, b):
    fa = float(str(a).replace(",", "."))
    fb = float(str(b).replace(",", "."))
    if fa == fb:
        return None
    return b if fb > fa else a