class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, n=None):
        self._element = element
        self._next = n


if __name__ == '__main__':
    n = _Node(10)
    print(n._element)
    n2 = _Node(20)
    n._next = n2
    print(n._element,n._next, n._next._element)
