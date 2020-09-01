# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                min_node = self.find_min_node(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, root.val)
        return root

    def find_min_node(self, root: TreeNode) -> TreeNode:
        curr = root
        while curr.left:
            curr = curr.left
        return curr