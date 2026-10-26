def is_nested(string):
    p = [1, 0, 0, 0, 0]
    for c in string:
        if c == '[':
            p[2] += p[1]
            p[1] += p[0]
        elif c == ']':
            p[4] += p[3]
            p[3] += p[2]
    return p[4] > 0