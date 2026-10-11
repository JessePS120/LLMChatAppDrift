def tri(n):
    if n < 0:
        return []
    size = max(n + 2, 2)
    res = [0] * size
    for i in range(size):
        if i == 1:
            res[i] = 3
        elif i % 2 == 0:
            res[i] = 1 + i // 2
    for i in range(size):
        if i % 2 != 0 and i != 1:
            res[i] = res[i - 1] + res[i - 2] + res[i + 1]
    return res[:n + 1]