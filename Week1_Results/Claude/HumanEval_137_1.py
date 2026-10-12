def compare_one(a, b):
    def to_float(x):
        if isinstance(x, str):
            return float(x.replace(',', '.'))
        return float(x)
    
    a_float = to_float(a)
    b_float = to_float(b)
    
    if a_float == b_float:
        return None
    elif a_float > b_float:
        return a
    else:
        return b