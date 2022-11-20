class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, e, n=None):
        self._element = e
        self._next = n


class LikedList:
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

        while p:
            print(p._element, end='=>')
            p = p._next
        print()

    def search(self, key):
        p = self._head
        index = 0

        while p:
            if p._element == key:
                return index

            p = p._next
            index += 1

        return -1

    def add_last(self, e):
        newest = _Node(e)

        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def add_first(self, e):
        newest = _Node(e)

        if self.is_empty():
            self._head = self._tail = newest
        else:
            newest._next = self._head
            self._head = newest

        self._size += 1

    def add_any(self, e, pos):
        p = self._head
        newest = _Node(e)
        i = 0
        while i < pos - 1:
            p = p._next
            i += 1

        newest._next = p._next
        p._next = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            print('List is Empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None
        return e

    def remove_last(self):
        if self.is_empty():
            print('List is Empty')
            return
        p = self._head
        i = 1
        while i < len(self) - 1:
            p = p._next
            i += 1

        self._tail = p
        p = p._next
        e = p._element
        self._tail._next = None
        self._size -= 1

        return e

    def remove_any(self, pos):
        if self.is_empty():
            print('List is Empty')
            return

        p = self._head
        i = 1
        while i < pos - 1:
            p = p._next
            i += 1

        e = p._next._element
        p._next = p._next._next
        self._size -= 1

        return e


if __name__ == '__main__':
    ll = LikedList()

    ll.add_first(5)
    ll.add_last(10)
    ll.add_last(20)
    ll.add_last(30)
    ll.add_last(40)
    ll.add_first(0)
    ll.add_any(25, 4)
    ll.remove_first()
    print(ll.remove_last())
    print(ll.remove_any(3))
    ll.display()
    print(len(ll))
    print(ll.search(40))

