def is_nested(string):
    opens = 0
    for i, c in enumerate(string):
        if c == '[':
            opens += 1
            if opens == 2:
                return string[i+1:].count(']') >= 2
    return False