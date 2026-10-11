from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two numbers in the list are closer to each other than the given threshold."""
    for i, num1 in enumerate(numbers):
        for num2 in numbers[i + 1:]:
            if abs(num1 - num2) < threshold:
                return True
    return False