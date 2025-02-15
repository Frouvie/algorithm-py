from typing import TypeVar, Callable, List, Optional

T = TypeVar('T')

def lower_bound(array: List[T], target: T, left: Optional[T] = None, right: Optional[T] = None, cmp: Callable[[T, T], bool] = lambda a, b : a < b) -> int:
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    while right - left > 1:
        mid = left + (right - left) // 2

        if cmp(array[mid], target):
            left = mid
        else:
            right = mid
    
    return right if cmp(array[right], target) else left

def lower_bound_desc(array: List[T], target: T, left: Optional[T] = None, right: Optional[T] = None, cmp: Callable[[T, T], bool] = lambda a, b : a < b) -> int:
    result = lower_bound(array[:].reverse(), target, left, right, cmp)

    return len(array) - 1 - result
