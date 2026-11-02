def order_by_points(nums):
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))
    return [x for _, x in sorted(((digit_sum(n), i, n) for i, n in enumerate(nums)), key=lambda t: (t[0], t[1]))]