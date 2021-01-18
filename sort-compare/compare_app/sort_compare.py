import quicksort
import bubblesort
import mergesort
from threading import Thread
import time




def track_quick(array, first, last):  # track the time for quick sort
    startq = time.process_time()
    quicksort.quick_sort(array, first, last)
    endq = time.process_time()
    return endq-startq


def track_merge(array):  # track the time for merge sort
    startm = time.process_time()
    mergesort.mergeSort(array)
    endm = time.process_time()
    return endm-startm


def track_bubble(array):  # track the time for bubble sort
    startb = time.process_time()
    bubblesort.bubbleSort(array)
    endb = time.process_time()
    return endb-startb


