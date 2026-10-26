def compare_one(a, b):
    def to_float(x):
        if isinstance(x, str):
            return float(x.replace(',', '.'))
        return float(x)
    
    va = to_float(a)
    vb = to_float(b)
    
    if va > vb:
        return a
    elif vb > va:
        return b
    else:
        return None