from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current = []
    depth = 0
    for ch in paren_string:
        if ch == '(':
            depth += 1
            current.append(ch)
        elif ch == ')':
            depth -= 1
            current.append(ch)
            if depth == 0:
                groups.append(''.join(current))
                current = []
    return groups