def is_nested(string):
    n = len(string)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = string[i:j]
            depth = 0
            max_depth = 0
            valid = True
            
            for char in substring:
                if char == '[':
                    depth += 1
                    max_depth = max(max_depth, depth)
                elif char == ']':
                    depth -= 1
                    if depth < 0:
                        valid = False
                        break
            
            if valid and depth == 0 and max_depth >= 2:
                return True
    
    return False