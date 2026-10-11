def is_nested(string):
    depth = 0
    for char in string:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
            if depth >= 2:
                return True
    return False