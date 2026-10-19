def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    min_val = min(a, b)
    max_val = max(a, b)
    result = []
    for i in range(min_val, max_val + 1):
        if i % 2 == 0 and i < 10:
            result.append(i)
    return result