from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current = []
    depth = 0

    for char in paren_string:
        if char == ' ':
            continue
        if char == '(':
            current.append(char)
            depth += 1
        elif char == ')':
            current.append(char)
            depth -= 1
            if depth == 0:
                groups.append(''.join(current))
                current = []

    return groups