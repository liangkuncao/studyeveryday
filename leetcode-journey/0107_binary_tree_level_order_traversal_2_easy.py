# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        def helper(root: TreeNode, res: List[List[int]], depth: int):
            if not root:
                return None

            if len(res) == depth:
                res.append([])

            res[depth].append(root.val)
            helper(root.left, res, depth + 1)
            helper(root.right, res, depth + 1)

        res = []
        helper(root, res, 0)
        return [l for l in reversed(res)]