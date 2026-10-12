def compare_one(a, b):
    def to_float(val):
        if isinstance(val, str):
            return float(val.replace(',', '.'))
        return float(val)
    
    fa = to_float(a)
    fb = to_float(b)
    
    if fa == fb:
        return None
    return a if fa > fb else b