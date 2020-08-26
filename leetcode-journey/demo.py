class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def merge_binary_tree(root1: Node, root2: Node) -> Node:
    if not root1:
        return root2
    if not root2:
        return root1
    root1.val += root2.val
    root1.left = merge_binary_tree(root1.left, root2.left)
    root1.right = merge_binary_tree(root1.right, root2.right)
    return root1