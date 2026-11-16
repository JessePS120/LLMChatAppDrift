def is_nested(string):
    stack = []
    best = 0
    for ch in string:
        if ch == '[':
            stack.append(ch)
        elif ch == ']' and stack:
            stack.pop()
            if len(stack) >= 1:
                best = max(best, len(stack) + 1)
    return best >= 2