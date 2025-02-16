from typing import TypeVar, List, Callable
from data_structures import Node

T = TypeVar('T')

class SegmentTree():
    def __init__(self, root: Node, neutral: T = 0, combine: Callable[[T, T], T] = lambda a, b : a + b):
        self.root = root
        self.neutral = neutral
        self.combine = combine
    
    def build_tree(self, array: List[T], current: Node, tl: int, tr: int) -> None:
        if tl == tr:
            current.value = array[tl]
        else:
            tm = tl + (tr - tl) // 2

            self.build_tree(array, current.left, tl, tm)
            self.build_tree(array, current.right, tm + 1, tr)

            current.value = self.combine(current.left.value, current.right.value)

    def update(self, current: Node, idx: int, value: T, tl: int, tr: int) -> None:
        if idx == tl == tr:
            current.value = value
            return
        
        if tr < idx or idx < tl:
            return
        
        tm = tl + (tr - tl) // 2

        self.update(current.left, idx, value, tl, tm)
        self.update(current.right, idx, value, tm + 1, tr)

        self.combine(current.left.value, current.right.value)

    def get(self, current: Node, l: int, r: int, tl: int, tr: int) -> T:
        if l <= tl and tr <= r:
            return current.value
        
        if tr < l or r < tl:
            return self.neutral
        
        tm = tl + (tr - tl) // 2

        return self.combine(self.get(current.left, l, r, tl, tm),
                            self.get(current.right, l, r, tm + 1, tr))