def is_nested(string):
    depth = 0
    for char in string:
        if char == '[':
            depth += 1
            if depth >= 2:
                return True
        else:
            depth -= 1
            if depth < 0:
                depth = 0
    return False