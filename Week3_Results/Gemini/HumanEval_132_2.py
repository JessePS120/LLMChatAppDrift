def is_nested(string):
    stack = []
    pairs = []
    for i, c in enumerate(string):
        if c == '[':
            stack.append(i)
        elif stack:
            pairs.append((stack.pop(), i))
    for s1, e1 in pairs:
        for s2, e2 in pairs:
            if s2 < s1 and e1 < e2:
                return True
    return False