class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        seq1 = self.get_leaves(root1)
        seq2 = self.get_leaves(root2)
        return True if seq1 == seq2 else False

    def get_leaves(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.get_leaves(root.left) + self.get_leaves(root.right)