def is_nested(string):
    balance = 0
    for char in string:
        if char == '[':
            balance += 1
        elif balance > 0:
            balance -= 1
            if balance > 0:
                return True
    return False