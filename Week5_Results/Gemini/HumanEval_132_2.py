def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(False)
        else:
            if stack:
                inner_has_nested = stack.pop()
                if stack:
                    stack[-1] = True
                if inner_has_nested:
                    return True
    return False