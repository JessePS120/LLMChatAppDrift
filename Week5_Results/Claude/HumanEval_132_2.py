def is_nested(string):
    pattern = '[[]]'
    s = 0
    for c in string:
        if s < len(pattern) and c == pattern[s]:
            s += 1
    return s == len(pattern)