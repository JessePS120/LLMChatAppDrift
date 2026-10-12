def is_nested(string):
    n = len(string)
    for i in range(n):
        if string[i] == '[':
            for j in range(i + 1, n):
                if string[j] == '[':
                    if string[j + 1:].count(']') >= 2:
                        return True
    return False