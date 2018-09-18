"""Sorting algorithms."""


def qsort(arr):
    """A QuickSort Algorithm.

    Author:
        zangw: http://stackoverflow.com/users/3011380/zangw
    References:
        http://stackoverflow.com/questions/18262306/quick-sort-with-python
    Alternate Implementations:
    # 1. Non-DRY
    def qsort(arr):
        if len(arr) <= 1:
            return arr
        return qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort(
            [x for x in arr[1:] if x >= arr[0]])
    """
    from operator import gt, le

    def compare(operator):
        """Comparison."""
        return [x for x in arr[1:] if operator(x, arr[0])]

    ops = {'>': gt, '<=': le}

    return arr if len(arr) <= 1 \
        else qsort(compare(ops['>'])) + [arr[0]] + qsort(compare(ops['<=']))
