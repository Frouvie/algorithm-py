def upper_bound(array, target, comparator = lambda a, b : a <= b):
    left = 0
    right = len(array) - 1

    while left < right:
        middle = left + (right - left) // 2

        if comparator(array[middle], target):
            left = middle + 1
        else:
            right = middle

    return left