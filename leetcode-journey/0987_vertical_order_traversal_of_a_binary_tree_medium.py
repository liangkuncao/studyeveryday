# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = defaultdict(list)
        def dfs(root: TreeNode, x: int, y: int) -> None:
            if not root:
                return
            nodes[x].append((root.val, y))
            dfs(root.left, x-1, y+1)
            dfs(root.right, x+1, y+1)
        dfs(root, 0, 0)
        return [[n[0] for n in sorted(nodes[k], key=lambda x:(x[1], x[0]))]
                for k in sorted(nodes.keys())]