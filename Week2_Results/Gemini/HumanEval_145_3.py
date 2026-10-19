def order_by_points(nums):
    def weight(n):
        neg = -1 if n < 0 else 1
        s = 0
        n_str = str(abs(n))
        for i, c in enumerate(n_str):
            if i == 0:
                s += int(c) * neg
            else:
                s += int(c)
        return s
    return sorted(nums, key=lambda x: (weight(x), nums.index(x)))