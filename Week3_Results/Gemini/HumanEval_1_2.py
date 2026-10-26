from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    cleaned = paren_string.replace(' ', '')
    result = []
    current = []
    depth = 0
    for char in cleaned:
        current.append(char)
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        if depth == 0:
            result.append(''.join(current))
            current = []
    return result