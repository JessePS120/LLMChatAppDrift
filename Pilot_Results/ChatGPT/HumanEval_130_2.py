def tri(n):
    """Return the first n + 1 numbers of the Tribonacci sequence."""
    if n < 0:
        return []

    result = [0] * (n + 1)

    for i in range(n + 1):
        if i == 1:
            result[i] = 3
        elif i % 2 == 0:
            result[i] = 1 + i // 2
        else:
            result[i] = result[i - 1] + result[i - 2] + result[i + 1] if i + 1 <= n else 0

    if n >= 3:
        for i in range(3, n + 1, 2):
            result[i] = result[i - 1] + result[i - 2] + result[i + 1]

    return result