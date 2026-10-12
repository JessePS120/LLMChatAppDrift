def is_nested(string):
    depth = 0
    has_nested = False
    
    for char in string:
        if char == '[':
            depth += 1
            if depth > 1:
                has_nested = True
        elif char == ']':
            if depth == 0:
                break
            depth -= 1
    
    return has_nested