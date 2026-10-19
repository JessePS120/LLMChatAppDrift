def order_by_points(nums):
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))
    
    indexed = [(num, i) for i, num in enumerate(nums)]
    indexed.sort(key=lambda x: (digit_sum(x[0]), x[1]))
    return [num for num, _ in indexed]