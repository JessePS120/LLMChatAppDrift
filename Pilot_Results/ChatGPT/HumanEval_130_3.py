def tri(n):
    """Return the first n + 1 numbers of the Tribonacci sequence."""
    result = []

    for i in range(n + 1):
        if i == 0:
            result.append(3)
        elif i % 2 == 0:
            result.append(1 + i / 2)
        else:
            result.append(result[i - 1] + result[i - 2] + (1 + (i + 1) / 2))

    return result