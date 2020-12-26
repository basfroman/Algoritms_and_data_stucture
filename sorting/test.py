import time
from sorting import babble_sort, choise_sort, insert_sort


def time_wrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print("Function ", func.__name__, " took ",
              round(float((stop - start)), 3), " seconds.\n")
        return result

    return wrapper


@time_wrapper
def sort_test(sort_algorithm):
    print("Test: ", sort_algorithm.__doc__)

    print("testcase #1: ", end="")
    arr = [4, 3, 2, 5, 1]
    arr_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(arr)
    print("Ok" if arr == arr_sorted else "Fail")

    print("testcase #2: ", end="")
    arr = list(range(10, 20)) + list(range(10))
    arr_sorted = list(range(20))
    sort_algorithm(arr)
    print("Ok" if arr == arr_sorted else "Fail")

    print("testcase #3: ", end="")
    arr = [4, 4, 2, 5, 1]
    arr_sorted = [1, 2, 4, 4, 5]
    sort_algorithm(arr)
    print("Ok" if arr == arr_sorted else "Fail")


if __name__ == '__main__':
    sort_test(babble_sort.sort)
    sort_test(choise_sort.sort)
    sort_test(insert_sort.sort)
