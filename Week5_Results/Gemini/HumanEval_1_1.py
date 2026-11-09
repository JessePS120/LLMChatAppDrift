from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current = []
    depth = 0
    for c in paren_string.replace(' ', ''):
        if c == '(':
            depth += 1
            current.append(c)
        elif c == ')':
            depth -= 1
            current.append(c)
            if depth == 0:
                result.append(''.join(current))
                current = []
    return result