def compare_one(a, b):
    def to_float(val):
        if isinstance(val, str):
            return float(val.replace(',', '.'))
        return float(val)
    
    float_a = to_float(a)
    float_b = to_float(b)
    
    if float_a == float_b:
        return None
    elif float_a > float_b:
        return a
    else:
        return b