from typing import TypeVar, List, Callable

T = TypeVar('T')

def merge_sort(array: List[T], cmp: Callable[[T, T], bool]) -> List[T]:
    pass