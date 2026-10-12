def is_nested(string):
    open_count = 0
    close_count = 0
    max_depth = 0
    
    for char in string:
        if char == '[':
            open_count += 1
            max_depth = max(max_depth, open_count - close_count)
        elif char == ']':
            close_count += 1
    
    return open_count >= close_count and max_depth >= 2