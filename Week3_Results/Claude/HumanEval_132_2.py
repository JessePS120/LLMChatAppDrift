def is_nested(string):
    n = len(string)
    for i in range(n):
        if string[i] == '[':
            depth = 0
            max_depth = 0
            for j in range(i, n):
                if string[j] == '[':
                    depth += 1
                    max_depth = max(max_depth, depth)
                elif string[j] == ']':
                    depth -= 1
                    if depth < 0:
                        break
                    if depth == 0:
                        if max_depth > 1:
                            return True
                        break
    return False