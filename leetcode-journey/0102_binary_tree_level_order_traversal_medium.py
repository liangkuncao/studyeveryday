# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        curr_level, next_level = [root], []
        while curr_level:
            curr_vals = []
            for node in curr_level:
                curr_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(curr_vals)
            curr_level, next_level = next_level, []
        return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        levels = [[root]]
        for level in levels:
            nodes = []
            for node in level:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if nodes:
                levels.append(nodes)
        return [[node.val for node in level] for level in levels]


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def get_level(root: TreeNode, res, depth):
            if not root:
                return None

            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            get_level(root.left, res, depth + 1)
            get_level(root.right, res, depth + 1)

        get_level(root, res, 0)
        return res
