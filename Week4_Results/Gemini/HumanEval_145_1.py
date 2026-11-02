def order_by_points(nums):
    def digits_sum(n):
        neg = -1 if n < 0 else 1
        return sum(int(digit) for digit in str(abs(n))) * neg
    return sorted(nums, key=lambda x: (digits_sum(x), nums.index(x)))