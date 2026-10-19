def is_nested(string):
    states = {(0, False)}
    
    for char in string:
        new_states = set()
        for depth, has_nested in states:
            if char == '[':
                new_depth = depth + 1
                new_nested = has_nested or (new_depth > 1)
                new_states.add((new_depth, new_nested))
            else:
                if depth > 0:
                    new_states.add((depth - 1, has_nested))
        states = new_states
    
    return (0, True) in states