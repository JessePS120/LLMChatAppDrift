def is_nested(string):
    state = 0
    for char in string:
        if state == 0 and char == '[':
            state = 1
        elif state == 1 and char == '[':
            state = 2
        elif state == 2 and char == ']':
            state = 3
        elif state == 3 and char == ']':
            return True
    return False