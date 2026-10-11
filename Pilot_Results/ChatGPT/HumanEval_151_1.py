def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    If the input list is empty, return 0.
    '''
    return sum(x ** 2 for x in lst if isinstance(x, int) and not isinstance(x, bool) and x > 0 and x % 2 == 1)