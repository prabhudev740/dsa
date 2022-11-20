class StacksList:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data == []

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            print('dsa05_Stack Is Empty')
            return
        return self._data.pop()

    def top(self):
        return self._data[-1]


if __name__ == '__main__':
    s = StacksList()

    print(s.is_empty())
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.top(), len(s))
    print(s.pop())
    print(s.top(), len(s))
    print(s.is_empty())
