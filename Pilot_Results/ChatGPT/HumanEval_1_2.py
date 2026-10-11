from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate groups of nested parentheses into individual strings.

    Ignore all spaces in the input string.
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