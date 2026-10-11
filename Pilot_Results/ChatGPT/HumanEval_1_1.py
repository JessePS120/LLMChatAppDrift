from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate balanced groups of nested parentheses into individual strings,
    ignoring spaces in the input.
    """
    groups = []
    current_group = []
    depth = 0

    for char in paren_string:
        if char == " ":
            continue

        current_group.append(char)

        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1