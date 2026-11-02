def is_nested(string):
    d = m = 0
    for c in string:
        if c == '[':
            d += 1
            m = max(m, d)
        elif c == ']':
            d -= 1
    return m >= 2