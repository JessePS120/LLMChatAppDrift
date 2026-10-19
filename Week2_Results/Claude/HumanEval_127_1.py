def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    
    length = intersection_end - intersection_start
    
    if length <= 0:
        return "NO"
    
    if length < 2:
        return "NO"
    
    if length == 2:
        return "YES"
    
    if length % 2 == 0:
        return "NO"
    
    for i in range(3, int(length**0.5) + 1, 2):
        if length % i == 0:
            return "NO"
    
    return "YES"