def is_nested(string):
    opens = 0
    closed_count = 0
    total_closes = string.count(']')
    for c in string:
        if c == '[':
            opens += 1
        else:
            closed_count += 1
            if opens >= 2 and closed_count < total_closes:
                return True
    return False