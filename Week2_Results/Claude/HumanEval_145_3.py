def order_by_points(nums):
    indexed = list(enumerate(nums))
    sorted_indexed = sorted(indexed, key=lambda x: (sum(int(d) for d in str(abs(x[1]))), x[0]))
    return [num for idx, num in sorted_indexed]