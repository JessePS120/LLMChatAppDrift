def order_by_points(nums):
    def digits_sum(n):
        digits = [int(c) for c in str(abs(n))]
        digits[0] *= -1 if n < 0 else 1
        return sum(digits)
    return sorted(nums, key=digits_sum)