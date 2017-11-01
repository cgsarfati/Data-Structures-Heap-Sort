"""Various implementations of heap sort.

>>> heap_sort_builtin([1, 5, 3, 7, 5, 8, 9, 0, 4])
[0, 1, 3, 4, 5, 5, 7, 8, 9]

>>> heap_sort_priority_queue([(1, 'J'), (4, 'N'), (3, 'H'), (2, 'O')])
J O H N

>>> heap_sort([4, 5, 3, 1, 3])
[1, 3, 3, 4, 5]

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


def heap_sort(lst):
    """Add items to binary heap (keeping them in order!) and then extract."""

    def move_down(first, last):
        """Move item down in heap to proper place."""

        # Assume left-hand child is bigger
        largest = 2 * first + 1

        while largest <= last:
            if largest < last and lst[largest] < lst[largest + 1]:
                # Right child exists and is larger than left child
                largest += 1

            if lst[largest] > lst[first]:
                # Selected child is bigger than parent, so swap
                lst[largest], lst[first] = lst[first], lst[largest]

                # Move down to largest child
                first = largest
                largest = 2 * first + 1

            else:
                # Once we don't swap, it's in the right place; exit
                return

    # Convert lst to heap

    length = len(lst) - 1
    least_parent = length // 2

    for i in range(least_parent, -1, -1):
        move_down(i, length)

    # Flatten heap into sorted array

    for i in range(length, 0, -1):
        if lst[0] > lst[i]:
            lst[0], lst[i] = lst[i], lst[0]
            move_down(0, i - 1)

    return lst


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "All tests passed!"
