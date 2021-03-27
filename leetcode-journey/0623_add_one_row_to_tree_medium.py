# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        cur_level = [root]
        while cur_level:
            d -= 1
            if d == 1:
                for node in cur_level:
                    left, right = node.left, node.right
                    node.left, node.right = TreeNode(v), TreeNode(v)
                    node.left.left = left
                    node.right.right = right
                return root
            next_level = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
