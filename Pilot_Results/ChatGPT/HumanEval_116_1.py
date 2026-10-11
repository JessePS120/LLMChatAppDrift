def sort_array(arr):
    """
    Sort an array by the number of ones in each integer's binary representation,
    in ascending order. For equal counts, sort by decimal value.
    """
    return sorted(arr, key=lambda x: (abs(x).bit_count(), x))