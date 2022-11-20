class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, e, left=None, right=None):
        self._element = e
        self._left = left
        self._right = right


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self, troot, e):
        temp = None

        while troot:
            temp = troot
            if e == troot._element:
                return
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right

        n = _Node(e)

        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n

    def rinsert(self, troot, e):
        if troot:
            if e < troot._element:
                troot._left = self.rinsert(troot._left, e)
            elif e > troot._element:
                troot._right = self.rinsert(troot._right, e)
        else:
            n = _Node(e)
            troot = n
        return troot

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
            self.postorder(troot._right)
            print(troot._element, end=' ')


    def isearch(self, troot, key):
        while troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                troot = troot._left
            else:
                troot = troot._right

        return False

    def rsearch(self, troot, key):
        if troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                return self.rsearch(troot._left, key)
            else:
                return self.rsearch(troot._right, key)
        return False

    def delete(self, e):
        p = self._root
        pp = None
        while pp and p._element != e:
            pp = p
            if e < p._element:
                p = p._left
            else:
                p = p._right

        if not p:
            return False
        if p._left and p._right:
            s = p._left
            ps = p
            while s._right:
                ps = s
                s = s._right
            p._element = s._element
            p = s
            pp = ps

        c = None
        if p._left:
            c = p._left
        else:
            c = p._right
        if p == self._root:
            self._root = None
        else:
            if p == pp._left:
                pp._left = c
            if p == pp._right:
                pp._right = c


def height(root):
    def sy(root):
        if root:
            x = sy(root.left)
            y = sy(root.right)

            if x > y:
                return x + 1
            else:
                return y + 1

        return 0

    return sy(root) - 1


if __name__ == '__main__':
    z = BinarySearchTree()

    z._root = z.rinsert(z._root, 3) # Here in recursive method first root will be NULL so , we have assign it as root
    # z.insert(z._root, 50)
    # z.insert(z._root, 30)
    # z.insert(z._root, 60)
    # z.insert(z._root, 10)
    # z.rinsert(z._root, 40)
    # z.rinsert(z._root, 20)
    z.rinsert(z._root, 5)
    z.rinsert(z._root, 2)
    z.rinsert(z._root, 1)
    z.rinsert(z._root, 4)
    z.rinsert(z._root, 6)
    z.rinsert(z._root, 7)

    # z.inorder(z._root)
    # print()
    # # print(z.isearch(z._root, 10))
    # # print(z.rsearch(z._root, 10))
    #
    # z.delete(10)
    # z.inorder(z._root)
    print(height(z._root))



    print(height(tree.root)-1)
