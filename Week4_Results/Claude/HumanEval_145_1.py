def order_by_points(nums):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = -n, -1
        digits = [int(d) for d in str(n)]
        digits[0] *= neg
        return sum(digits)
    return sorted(nums, key=digits_sum)