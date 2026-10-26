from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    cleaned = paren_string.replace(' ', '')
    result = []
    current_group = ''
    balance = 0
    
    for char in cleaned:
        current_group += char
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            result.append(current_group)
            current_group = ''
    
    return result