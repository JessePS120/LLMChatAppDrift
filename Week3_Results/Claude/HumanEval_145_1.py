def order_by_points(nums):
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))
    
    return sorted(enumerate(nums), key=lambda x: (digit_sum(x[1]), x[0]))[1] if nums else []