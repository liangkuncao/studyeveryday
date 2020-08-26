# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def sum_of_left_leaves(root: TreeNode, flag: bool) -> int:
            if not root:
                return 0
            elif not root.left and not root.right:
                return root.val if flag else 0
            return sum_of_left_leaves(root.left, True) + sum_of_left_leaves(root.right, False)

        return sum_of_left_leaves(root, False)