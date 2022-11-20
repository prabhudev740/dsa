class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, e, n=None):
        self._element = e
        self._next = n

class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def display(self):
        p = self._head

        i = 0
        while i < self._size:
            print(p._element, end='=>')
            p = p._next
            i += 1
        print()

    def add_last(self, e):
        newest = _Node(e)
        if self.is_empty():
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def add_first(self, e):
        newest = _Node(e)

        if self.is_empty():
            newest._next = newest
            self._head= self._tail = newest
        else:
            self._tail._next = newest
            newest._next = self._head
        self._head = newest
        self._size += 1


if __name__ == '__main__':
    cll = CircularLinkedList()

    cll.add_last(10)
    cll.add_last(20)
    cll.add_last(30)
    cll.add_last(40)

    cll.add_first(1)

    cll.display()
    print(len(cll))
