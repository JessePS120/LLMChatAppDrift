def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(0)
        else:
            if stack:
                inner = stack.pop()
                if stack:
                    stack[-1] += 1
                if inner > 0:
                    return True
    return False