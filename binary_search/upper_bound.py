from typing import TypeVar, Callable, List, Optional

T = TypeVar('T')

def upper_bound(array: List[T], target: T, left: Optional[T] = None, right: Optional[T] = None, cmp: Callable[[T, T], bool] = lambda a, b : a <= b) -> int:
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    while left < right:
        mid = left + (right - left) // 2

        if cmp(array[mid], target):
            left = mid + 1
        else:
            right = mid

    return left if cmp(array[right], target) else right

def upper_bound_desc(array: List[T], target: T, left: Optional[T] = None, right: Optional[T] = None, cmp: Callable[[T, T], bool] = lambda a, b : a <= b) -> int:
    result = upper_bound(array[:].reverse(), target, left, right, cmp)

    return len(array) - 1 - result
