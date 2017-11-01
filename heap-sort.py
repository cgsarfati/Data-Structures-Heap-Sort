"""Various implementations of heap sort.

>>> heap_sort_builtin([1, 5, 3, 7, 5, 8, 9, 0, 4])
[0, 1, 3, 4, 5, 5, 7, 8, 9]
"""

from heapq import heappush, heappop, heapify


def heap_sort_builtin(lst, heap=[]):
    """Built-in python module.

    heappop = extracts min value from lst
    heappush = puts data into heap
    """

    for item in lst:
        heappush(heap, item)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "All tests passed!"
