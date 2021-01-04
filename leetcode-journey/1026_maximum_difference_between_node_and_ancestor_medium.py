# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, min_: int, max_: int, res: int) -> int:
            min_, max_ = min(min_, node.val), max(max_, node.val)
            if not node.left and not node.right:
                res = max(res, abs(min_ - max_))
                return res
            if node.left:
                res = dfs(node.left, min_, max_, res)
            if node.right:
                res = dfs(node.right, min_, max_, res)
            return res

        res = dfs(root, root.val, root.val, 0)
        return res
