# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, 0)]
        while stack:
            root, num = stack.pop()
            if root:
                num = (num << 1) | root.val
                if not root.left and not root.right:
                    res += num
                else:
                    stack.append((root.left, num))
                    stack.append((root.right, num))
        return res