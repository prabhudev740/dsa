class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, e, n=None):
        self._element = e
        self._next = n


class StackLined:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        newest = _Node(e)
        if self.is_empty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self.is_empty():
            print('dsa05_Stack is Empty')
            return

        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e

    def top(self):
        if self.is_empty():
            print('dsa05_Stack is Empty')
            return
        return self._top._element


if __name__ == '__main__':
    s = StackLined()

    print(s.is_empty())
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.top(), len(s))
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.top(), len(s))
    print(s.is_empty())

