def order_by_points(nums):
    return sorted(nums, key=lambda n: sum(int(digit) for digit in str(abs(n))))