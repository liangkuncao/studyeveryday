# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        curr_stack, next_stack = {root: None}, {}
        while curr_stack:
            x_node, y_node, x_parent, y_parent = None, None, None, None
            for node, parent in curr_stack.items():
                if node.val == x:
                    x_node, x_parent = node, parent
                elif node.val == y:
                    y_node, y_parent = node, parent

                if node.left:
                    next_stack[node.left] = node
                if node.right:
                    next_stack[node.right] = node
            if x_node and y_node:
                if x_parent != y_parent:
                    return True
                return False
            elif x_node:
                return False
            elif y_node:
                return False

            curr_stack, next_stack = next_stack, {}
        return False


