# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def helper_dfs(root: TreeNode) -> List[int]:
            if not root:
                return []
            res = []
            res += helper_dfs(root.left)
            res.append(root.val)
            res += helper_dfs(root.right)
            return res

        list1 = helper_dfs(root1)
        list2 = helper_dfs(root2)
        res = []
        while list1 and list2:
            if list1[0] <= list2[0]:
                res.append(list1.pop(0))
            else:
                res.append(list2.pop(0))
        if list1:
            res += list1
        if list2:
            res += list2
        return res