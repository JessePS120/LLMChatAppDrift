def is_nested(string):
    state = 0
    for c in string:
        if c == '[':
            if state < 2:
                state += 1
        elif c == ']':
            if state == 1:
                state = 0
            elif state == 2:
                state = 3
            elif state == 3:
                return True
    return False