def is_nested(string):
    stack = []
    pairs = []
    for idx, char in enumerate(string):
        if char == '[':
            stack.append(idx)
        elif char == ']' and stack:
            start = stack.pop()
            pairs.append((start, idx))
    for u, v in pairs:
        for i, j in pairs:
            if u < i and j < v:
                return True
    return False