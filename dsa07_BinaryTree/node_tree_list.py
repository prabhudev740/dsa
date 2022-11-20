class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def append_child(self, node):
        self.children.append(node)


root = TreeNode("drink")
hot = TreeNode("Hot")
cold = TreeNode("cold")
root.append_child(hot)
root.append_child(cold)

sprite = TreeNode("Sprite")
mazza = TreeNode("Mazza")
tea = TreeNode("tea")
cofee = TreeNode("Cofee")

hot.append_child(tea)
hot.append_child(cofee)
cold.append_child(sprite)
cold.append_child(mazza)

