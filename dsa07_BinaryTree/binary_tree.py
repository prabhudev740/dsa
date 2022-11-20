from dsa06_QueueADT.queue_linked import QueueLinked


class _Node:
    __slots__ = '_element', '_left', '_right'  # efficiently allocate memory for instance variable

    def __init__(self, e, left=None, right=None):
        self._element = e
        self._left = left
        self._right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def make_tree(self, e, left, right):
        self._root = _Node(e, left._root, right._root)

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=' ')
            self.inorder(troot._right)

    def preorder(self, troot):
        if troot:
            print(troot._element, end=' ')
            self.preorder(troot._left)
            self.preorder(troot._right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot._left)
            self.postorder((troot._right))
            print(troot._element, end=' ')

    def levelorder(self, troot):
        Q = QueueLinked()
        t = troot
        print(t._element, end=' ')
        Q.enqueue(t)

        while not Q.is_empty():
            t = Q.dequeue()

            if t._left:
                print(t._left._element, end=' ')
                Q.enqueue(t._left)

            if t._right:
                print(t._right._element, end=' ')
                Q.enqueue(t._right)

    def count(self, troot):
        if troot:
            x = self.count(troot._left)
            y = self.count(troot._right)
            return x + y + 1
        return 0

    def height(self, troot):  # we will get h + 1 height as result so, we need to - 1 to final result for correct value
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)

            if x > y:
                return x + 1
            else:
                return y + 1

        return 0

    def search(self, troot, key):
        res1 = False
        res2 = False
        if troot:
            if key == troot._element:
                return True
            res1 = self.search(troot._left, key)
            res2 = self.search(troot._right, key)
        return res1 or res2





def example_one():
    #          10
    #        /    \
    #      20      30

    x = BinaryTree()  # child: 20
    y = BinaryTree()  # child: 30
    z = BinaryTree()  # root: 10
    a = BinaryTree()  # Null for leaf node's child

    x.make_tree(20, a, a)
    y.make_tree(30, a, a)
    z.make_tree(10, x, y)

    print('In-Order Traversal', end=': ')
    z.inorder(z._root)
    print()
    print('Pre-Order Traversal', end=': ')
    z.preorder(z._root)
    print()
    print('Post-Order Traversal', end=': ')
    z.postorder(z._root)
    print()
    print('Level-Order Traversal', end=': ')
    z.levelorder(z._root)
    print()
    print('Node count: ', z.count(z._root))
    print('Height', z.height(z._root) - 1)

def example_two():
    # Example 2:-
    #       10(t)
    #     /    \
    #    20(z)  30(s)
    #   /      /
    #  40(x)  50(r)
    #           \
    #            60(y)

    x = BinaryTree()
    y = BinaryTree()
    z = BinaryTree()
    r = BinaryTree()
    s = BinaryTree()
    t = BinaryTree()
    a = BinaryTree()

    x.make_tree(40, a, a)
    y.make_tree(60, a, a)
    z.make_tree(20, x, a)
    r.make_tree(50, a, y)
    s.make_tree(30, r, a)
    t.make_tree(10, z, s)

    print('In-Order Traversal', end=': ')
    t.inorder(t._root)
    print()
    print('Pre-Order Traversal', end=': ')
    t.preorder(t._root)
    print()
    print('Post-Order Traversal', end=': ')
    t.postorder(t._root)
    print()
    print('Level-Order Traversal', end=': ')
    t.levelorder(t._root)
    print()
    print('Count Node:', t.count(t._root))
    print('Height:', t.height(t._root) - 1)
    print(t.search(t._root, 0))


if __name__ == '__main__':
    example_two()
