def compare_one(a, b):
    def to_number(x):
        if isinstance(x, str):
            return float(x.replace(',', '.'))
        return float(x)
    
    num_a = to_number(a)
    num_b = to_number(b)
    
    if num_a > num_b:
        return a
    elif num_b > num_a:
        return b
    else:
        return None