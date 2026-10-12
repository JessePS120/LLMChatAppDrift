def intersection(interval1, interval2):
    s = max(interval1[0], interval2[0])
    e = min(interval1[1], interval2[1])
    l = e - s
    if l < 2:
        return "NO"
    for i in range(2, int(l**0.5) + 1):
        if l % i == 0:
            return "NO"
    return "YES"