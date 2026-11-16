def order_by_points(nums):
    def digit_sum(n):
        s = [int(c) for c in str(n) if c != '-']
        if n < 0:
            s[0] = -s[0]
        return sum(s)
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))