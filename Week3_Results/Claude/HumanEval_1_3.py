from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    result = []
    current_group = ''
    balance = 0
    
    for char in paren_string:
        if char == '(':
            balance += 1
            current_group += char
        elif char == ')':
            balance -= 1
            current_group += char
            if balance == 0:
                result.append(current_group)
                current_group = ''
    
    return result