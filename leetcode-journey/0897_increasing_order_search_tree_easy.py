# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def help(root: TreeNode) -> List[TreeNode]:
            if not root:
                return []
            left, right = help(root.left), help(root.right)
            root.left, root.right = None, None
            return left + [root] + right

        dummy = TreeNode()
        cur = dummy
        for node in help(root):
            cur.right = node
            cur = node
        return dummy.right