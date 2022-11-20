class _TreeNode:
    __slots__ = '_data', '_left', '_right'

    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def make_tree(self, data, left=None, right=None):
        self._root = _TreeNode(data, left._root, right._root)

    def preorder(self, troot):
        if troot:
            print(troot._data, end = ' ')
            self.preorder(troot._left)
            self.preorder(troot._right)

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._data, end=' ')
            self.inorder(troot._right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._data, end=' ')

    def search(self, troot, key):
        res1 = False
        res2 = False
        if troot:
            if troot._data == key:
                return True
            res1 = self.search(troot._left, key)
            res2 = self.search(troot._right, key)
        return res1 or res2

    def count(self, troot):
        if troot:
            x = self.count(troot._left)
            y = self.count(troot._right)
            return x + y + 1
        return 0

    def height(self, troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0

def main():
    #     root
    #     /  \
    # left    right

    z = BinaryTree()  # root node
    left = BinaryTree()  # Left Node
    right = BinaryTree()  # right Node
    a = BinaryTree() # None for leaf node

    left.make_tree(20, a, a)
    right.make_tree(30, a, a)
    z.make_tree(10, left, right)

    print("Pre-Order Traversal")
    z.preorder(z._root)
    print()

    print("In-Order Traversal")
    z.inorder(z._root)
    print()

    print("Post-Order Traversal")
    z.postorder(z._root)
    print()
    print(z.search(z._root, 11))
    print(z.count(z._root))
    print(z.height(z._root))


if __name__ == "__main__":
    main()
