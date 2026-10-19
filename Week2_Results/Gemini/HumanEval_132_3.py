def is_nested(string):
    stack = []
    pairs = []
    for i, char in enumerate(string):
        if char == '[':
            stack.append(i)
        elif char == ']' and stack:
            start = stack.pop()
            pairs.append((start, i))
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            s1, e1 = pairs[i]
            s2, e2 = pairs[j]
            if (s1 < s2 and e2 < e1) or (s2 < s1 and e1 < e2):
                return True
    return False