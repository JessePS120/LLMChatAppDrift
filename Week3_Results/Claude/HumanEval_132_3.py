def is_nested(string):
    stack = []
    max_depth = 0
    
    for char in string:
        if char == '[':
            stack.append('[')
            max_depth = max(max_depth, len(stack))
        elif char == ']':
            if stack:
                stack.pop()
    
    return len(stack) == 0 and max_depth > 1