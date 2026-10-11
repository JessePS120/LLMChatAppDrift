def is_nested(string):
    stack = []
    pairs = []
    for i, char in enumerate(string):
        if char == '[':
            stack.append(i)
        elif char == ']':
            if stack:
                open_idx = stack.pop()
                pairs.append((open_idx, i))
    
    for c, d in pairs:
        for a, b in pairs:
            if c < a and b < d:
                return True
    return False