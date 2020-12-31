# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, path: List[TreeNode], count: List[int]) -> None:
            path.append(node)
            count[node.val] += 1
            if not node.left and not node.right:
                tmp = 0
                for i, x in enumerate(count):
                    if tmp > 1:
                        break
                    if x % 2 == 1:
                        tmp += 1
                if tmp <= 1:
                    nonlocal res
                    res += 1
            if node.left:
                dfs(node.left, path, count)
            if node.right:
                dfs(node.right, path, count)
            path.pop()
            count[node.val] -= 1

        res = 0
        path, count = [], [0] * 10
        dfs(root, path, count)
        return res