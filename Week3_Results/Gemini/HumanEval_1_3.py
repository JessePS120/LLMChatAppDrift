from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current = []
    depth = 0
    for c in paren_string:
        if c == ' ':
            continue
        current.append(c)
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        if depth == 0:
            result.append(''.join(current))
            current = []
    return result