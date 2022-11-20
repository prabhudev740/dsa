class DEQueList:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data == []

    def add_first(self, e):
        self._data.insert(0, e)

    def add_last(self, e):
        self._data.append(e)

    def remove_first(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._data.pop(0)

    def remove_last(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._data.pop()

    def first(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._data[0]

    def last(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._data[-1]


if __name__ =='__main__':
    d = DEQueList()

    print(d.is_empty())
    d.add_first(5)
    d.add_first(3)
    d.add_first(1)
    print(d._data, len(d), d.first(), d.last())
    d.add_last(10)
    d.add_last(20)
    print(d.remove_first())
    print(d._data, len(d), d.first(), d.last())
    print(d.remove_last())
    print(d._data, len(d), d.first(), d.last())
    print(d.remove_first())
    print(d._data, len(d), d.first(), d.last())

    print(d.is_empty())