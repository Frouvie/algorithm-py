from typing import TypeVar, List, Callable

T = TypeVar('T')

def quick_sort(array: List[T], cmp: Callable[[T, T], bool]) -> List[T]:
    pass