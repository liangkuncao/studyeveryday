# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:

        def helper(node: TreeNode):
            if not node:
                return
            if not node.left:
                val_sum_left = 0
                tilt_sum_left = 0
            else:
                helper(node.left)
                val_sum_left = node.left.val[1]
                tilt_sum_left = node.left.val[2]
            if not node.right:
                val_sum_right = 0
                tilt_sum_right = 0
            else:
                helper(node.right)
                val_sum_right = node.right.val[1]
                tilt_sum_right = node.right.val[2]
            tilt = abs(val_sum_left - val_sum_right)
            node.val = [tilt, val_sum_left + val_sum_right + node.val, tilt_sum_left + tilt_sum_right + tilt]

        if not root:
            return 0
        helper(root)
        return root.val[2]