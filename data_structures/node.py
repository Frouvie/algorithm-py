from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: Optional[T] = None, left: Optional['Node[T]'] = None, right: 'Node[T]' = None):
        self.value = value
        self.left = left
        self.right = right