import time


def split(array, first, last):
    shift = array[first]
    low = first + 1
    high = last

    while True:
        while low <= high and array[high] >= shift:
            high = high - 1

        while low <= high and array[low] <= shift:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[first], array[high] = array[high], array[first]

    return high


def quick_sort(array, first, last):
    start = time.time()
    if first >= last:
        return

    p = split(array, first, last)
    quick_sort(array, first, p-1)
    quick_sort(array, p+1, last)
