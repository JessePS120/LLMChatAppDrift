def is_nested(string):
    stack = []
    pairs = []
    for i, char in enumerate(string):
        if char == '[':
            stack.append(i)
        elif char == ']' and stack:
            pairs.append((stack.pop(), i))
    for s1, e1 in pairs:
        for s2, e2 in pairs:
            if s1 < s2 and e2 < e1:
                return True
    return False