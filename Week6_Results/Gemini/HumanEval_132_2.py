def is_nested(string):
    stack = []
    pairs = []
    for i, c in enumerate(string):
        if c == '[':
            stack.append(i)
        elif c == ']' and stack:
            pairs.append((stack.pop(), i))
    for c, d in pairs:
        for a, b in pairs:
            if c < a and b < d:
                return True
    return False