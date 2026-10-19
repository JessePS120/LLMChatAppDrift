def is_nested(string):
    depth = 0
    for char in string:
        if char == '[':
            depth += 1
        else:
            if depth > 1:
                return True
            depth -= 1
    return False