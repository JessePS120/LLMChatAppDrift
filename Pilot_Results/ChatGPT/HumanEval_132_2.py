def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    Return True if there is a valid subsequence of brackets where at least one bracket is nested.
    '''
    depth = 0

    for char in string:
        if char == '[':
            depth += 1
        elif char == ']':
            if depth > 1:
                return True
            if depth > 0:
                depth -= 1

    return False