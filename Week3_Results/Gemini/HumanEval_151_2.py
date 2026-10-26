def double_the_difference(lst):
    ans = 0
    for num in lst:
        if isinstance(num, int) and not isinstance(num, bool) and num > 0 and num % 2 == 1:
            ans += num ** 2
    return ans