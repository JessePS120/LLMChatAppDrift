from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current = []
    depth = 0

    for char in paren_string:
        if char == ' ':
            continue

        current.append(char)

        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1

            if depth == 0:
                groups.append(''.join(current))
                current = []

    return groups