
def sort(array):
    """Insert sort
    >>> sort([4, 3, 2, 5, 1])
    [1, 2, 3, 4, 5]
    >>> sort([_ for _ in range(10, 20)] + [_ for _ in range(10)])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    """
    for top in range(1, len(array)):
        k = top
        while k > 0 and array[k-1] > array[k]:
            array[k], array[k - 1] = array[k - 1], array[k]
            k -= 1
    return array


if __name__ == '__main__':
    import doctest
    doctest.testmod()
