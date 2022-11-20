class QueueList:
    def __init__(self):
        self._data = []

    def __len__(self):
        return  len(self._data)

    def is_empty(self):
        return self._data == []

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            print('dsa06_QueueADT is Empty')
            return
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            print('dsa06_QueueADT is Empty')
            return
        return self._data[0]


if __name__ == '__main__':
    q = QueueList()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.first(), len(q), q._data)
    print(q.dequeue())
    print(q.first(), len(q), q._data)
    print(q.is_empty())
