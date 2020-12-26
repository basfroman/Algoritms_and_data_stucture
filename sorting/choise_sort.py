def sort(array):
    """Choice sort"""
    for pos in range(0, len(array)):
        for k in range(pos + 1, len(array)):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]
    return array
