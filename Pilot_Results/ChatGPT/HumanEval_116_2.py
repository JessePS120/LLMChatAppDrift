def sort_array(arr):
    """
    In this Kata, sort an array of integers by the number of ones in their
    binary representation in ascending order. For equal counts, sort by
    decimal value.
    """
    return sorted(arr, key=lambda n: (bin(abs(n)).count('1'), n))