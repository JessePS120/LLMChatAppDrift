def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    length = end - start
    if length < 2:
        return "NO"
    i = 2
    while i * i <= length:
        if length % i == 0:
            return "NO"
        i += 1
    return "YES"