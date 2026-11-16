def is_nested(string):
    targets = '[[]]'
    state = 0
    for ch in string:
        if state < len(targets) and ch == targets[state]:
            state += 1
    return state == len(targets)