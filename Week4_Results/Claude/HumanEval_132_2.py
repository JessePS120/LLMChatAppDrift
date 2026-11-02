def is_nested(string):
    target = '[[]]'
    i = 0
    for c in string:
        if i < len(target) and c == target[i]:
            i += 1
    return i == len(target)