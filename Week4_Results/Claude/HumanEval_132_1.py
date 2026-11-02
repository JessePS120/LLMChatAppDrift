def is_nested(string):
    stack = []
    nested = False
    for c in string:
        if c == '[':
            stack.append(False)
        elif stack:
            has_child = stack.pop()
            if has_child:
                nested = True
            if stack:
                stack[-1] = True
    return nested