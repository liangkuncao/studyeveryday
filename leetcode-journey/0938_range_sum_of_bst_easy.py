# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def help(node: TreeNode):
            if node:
                if low <= node.val <= high:
                    self.res += node.val
                if low < node.val:
                    help(node.left)
                if node.val < high:
                    help(node.right)

        self.res = 0
        help(root)
        return self.res