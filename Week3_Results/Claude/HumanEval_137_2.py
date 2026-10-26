def compare_one(a, b):
    def to_float(x):
        if isinstance(x, str):
            return float(x.replace(',', '.'))
        return float(x)
    
    val_a = to_float(a)
    val_b = to_float(b)
    
    if val_a == val_b:
        return None
    elif val_a > val_b:
        return a
    else:
        return b