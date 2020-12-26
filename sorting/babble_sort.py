def sort(array):
    """Babble sort"""
    n = len(array)
    for bypass in range(1, n):
        for k in range(n - bypass):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
    return array
