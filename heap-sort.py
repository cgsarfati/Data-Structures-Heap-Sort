"""Various implementations of heap sort.

>>> heap_sort_builtin([1, 5, 3, 7, 5, 8, 9, 0, 4])
[0, 1, 3, 4, 5, 5, 7, 8, 9]

>>> heap_sort_priority_queue([(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')])
J O H N

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


def heap_sort_priority_queue(data, heap=[]):
    """Insert items at correct place in priority queue.

    In tuple, 1st item is queue placement. What is returned is 2nd item in tuple
    in chronological order based on queue."""

    for item in data:
        heappush(heap, item)

    while heap:
        print heappop(heap)[1],


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "All tests passed!"
