# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, cur: int = 0, total: int = 0) -> int:
            cur = cur * 10 + node.val
            if not node.left and not node.right:
                total += cur
                return total
            if node.left:
                total = dfs(node.left, cur, total)
            if node.right:
                total = dfs(node.right, cur, total)
            return total

        if not root:
            return 0
        res = dfs(root)
        return res