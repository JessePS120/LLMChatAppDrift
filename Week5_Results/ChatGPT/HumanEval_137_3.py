def compare_one(a, b):
    def to_float(value):
        if isinstance(value, str):
            value = value.replace(",", ".")
        return float(value)

    num_a = to_float(a)
    num_b = to_float(b)

    if num_a > num_b:
        return a
    if num_b > num_a:
        return b
    return None