# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        def dfs(node: TreeNode, row: int, col: int) -> None:
            if node:
                vals[col].append((row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        vals = defaultdict(list)
        dfs(root, 0, 0)
        res = []
        for col in sorted(vals.keys()):
            vals[col].sort(key=lambda x: (x[0], x[1]))
            res.append([val for _, val in vals[col]])
        return res