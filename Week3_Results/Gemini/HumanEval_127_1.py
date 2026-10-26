def intersection(interval1, interval2):
    s1, e1 = interval1
    s2, e2 = interval2
    start = max(s1, s2)
    end = min(e1, e2)
    length = end - start
    if length < 2:
        return "NO"
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return "NO"
    return "YES"