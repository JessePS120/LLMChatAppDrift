def tri(n):
    if n == 0:
        return [1]
    t = [0] * (n + 1)
    t[0] = 1
    if n >= 1:
        t[1] = 3
    for i in range(2, n + 1):
        if i % 2 == 0:
            t[i] = 1 + i // 2
        else:
            t[i] = t[i - 1] + t[i - 2] + (1 + (i + 1) // 2)
    return t