class _TreeNode:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, e, left=None, right=None):
        self._element = e
        self._left = left
        self._right = right


one = _TreeNode(10)
two = _TreeNode(20)
tree = _TreeNode(30, one, two)

print()