def order_by_points(nums):
    def digit_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        s = []
        while n > 0:
            s.append(n % 10)
            n //= 10
        s = s[::-1]
        if s:
            s[0] *= neg
        return sum(s)
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))