from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Input is a string containing multiple groups of nested parentheses.
    Separate the groups into individual strings, ignoring all spaces.
    """
    groups = []
    current_group = []
    depth = 0

    for char in paren_string:
        if char.isspace():
            continue

        current_group.append(char)

        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1

            if depth == 0:
                groups.append(''.join(current_group))
                current_group = []

    return groups