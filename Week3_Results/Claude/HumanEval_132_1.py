def is_nested(string):
    for i in range(len(string)):
        if string[i] == '[':
            depth = 0
            max_depth = 0
            for j in range(i, len(string)):
                if string[j] == '[':
                    depth += 1
                    max_depth = max(max_depth, depth)
                elif string[j] == ']':
                    depth -= 1
                    if depth == 0:
                        if max_depth >= 2:
                            return True
                        break
                    elif depth < 0:
                        break
    return False