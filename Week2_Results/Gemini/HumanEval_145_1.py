def order_by_points(nums):
    def digit_sum(n):
        s = [int(x) for x in str(n) if x != '-']
        if n < 0:
            s[0] = -s[0]
        return sum(s)
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))