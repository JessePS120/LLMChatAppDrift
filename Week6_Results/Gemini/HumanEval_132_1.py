def is_nested(string):
    stack = []
    pairs = []
    for i, c in enumerate(string):
        if c == '[':
            stack.append(i)
        elif c == ']' and stack:
            pairs.append((stack.pop(), i))
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            s1, e1 = pairs[i]
            s2, e2 = pairs[j]
            if (s1 < s2 and e2 < e1) or (s2 < s1 and e1 < e2):
                return True
    return False