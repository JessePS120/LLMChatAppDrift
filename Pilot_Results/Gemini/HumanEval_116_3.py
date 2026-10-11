def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x & 0xFFFFFFFF).count('1'), x))