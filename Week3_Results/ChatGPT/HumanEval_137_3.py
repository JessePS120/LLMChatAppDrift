def compare_one(a, b):
    def to_number(value):
        if isinstance(value, str):
            return float(value.replace(",", "."))
        return float(value)

    num_a = to_number(a)
    num_b = to_number(b)

    if num_a == num_b:
        return None
    return a if num_a > num_b else b