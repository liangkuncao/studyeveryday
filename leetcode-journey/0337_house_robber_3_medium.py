# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Tuple


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            rob[root] = root.val + no_rob[root.left] + no_rob[root.right]
            no_rob[root] = max(rob[root.left], no_rob[root.left]) + max(rob[root.right], no_rob[root.right])

        rob, no_rob = defaultdict(int), defaultdict(int)
        dfs(root)
        return max(rob[root], no_rob[root])