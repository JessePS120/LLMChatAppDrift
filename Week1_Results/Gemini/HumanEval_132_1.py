def is_nested(string):
    open_indices = [i for i, c in enumerate(string) if c == '[']
    close_indices = [i for i, c in enumerate(string) if c == ']']
    return len(open_indices) >= 2 and len(close_indices) >= 2 and open_indices[1] < close_indices[0]