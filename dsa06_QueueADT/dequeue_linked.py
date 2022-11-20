class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, e, n=None):
        self._element = e
        self._next = n


class DEQueLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def display(self):
        p = self._front

        while p:
            print(p._element, end='=>')
            p = p._next
        print()


    def add_last(self, e):
        newest = _Node(e)

        if self.is_empty():
            self._front = newest
        else:
            self._rear._next = newest

        self._rear = newest
        self._size += 1

    def add_first(self, e):
        newest = _Node(e)

        if self.is_empty():
            self._front = self._rear = newest
        else:
            newest._next = self._front
            self._front = newest

        self._size += 1

    def remove_first(self):
        if self.is_empty():
            print('List is Empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1

        if self.is_empty():
            self._rear = None
        return e

    def remove_last(self):
        if self.is_empty():
            print('List is Empty')
            return
        p = self._front
        i = 1
        while i < len(self) - 1:
            p = p._next
            i += 1

        self._rear = p
        p = p._next
        e = p._element
        self._rear._next = None
        self._size -= 1

        return e

    def first(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._front._element

    def last(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._rear._element


if __name__ =='__main__':
    d = DEQueLinked()

    print(d.is_empty())
    d.add_first(5)
    d.add_first(3)
    d.add_first(1)
    d.display()
    print(len(d), d.first(), d.last())
    d.add_last(10)
    d.add_last(20)
    d.display()
    print(d.remove_first())
    print(len(d), d.first(), d.last())
    print(d.remove_last())
    d.display()
    print(len(d), d.first(), d.last())
    print(d.remove_first())
    print(len(d), d.first(), d.last())
    d.display()


    print(d.is_empty())