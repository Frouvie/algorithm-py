from typing import TypeVar, Callable, List, Optional

T = TypeVar('T')

def upper_bound(array: List[T], target: T, left: Optional[T] = None, right: Optional[T] = None, comparator: Callable[[T, T], bool] = lambda a, b : a <= b) -> int:
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    while left < right:
        middle = left + (right - left) // 2

        if comparator(array[middle], target):
            left = middle + 1
        else:
            right = middle

    return left if comparator(array[right], target) else right