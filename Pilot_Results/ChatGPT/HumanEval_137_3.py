def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    def to_float(value):
        if isinstance(value, str):
            return float(value.replace(",", "."))
        return float(value)

    num_a = to_float(a)
    num_b = to_float(b)

    if num_a > num_b:
        return a
    elif num_b > num_a:
        return b
    return None