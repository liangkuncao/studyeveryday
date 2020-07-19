# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(root: TreeNode) -> List[TreeNode]:
            if not root:
                return []
            return helper(root.right) + helper(root.left) + [root]

        if not root:
            return

        stack = helper(root)

        curr = root
        stack.pop()
        while stack:
            curr.left = None
            curr.right = stack.pop()
            curr = curr.right
        return root


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            if stack:
                curr.right = stack[-1]
            curr.left = None
        return root
