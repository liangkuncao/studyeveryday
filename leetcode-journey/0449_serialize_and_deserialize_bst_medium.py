# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []

        def preorder(root: TreeNode) -> None:
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        return ' '.join(map(str, res))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nums = deque(int(n) for n in data.split())

        def build(mmin: int, mmax: int) -> None:
            if nums and mmin < nums[0] < mmax:
                n = nums.popleft()
                node = TreeNode(n)
                node.left = build(mmin, n)
                node.right = build(n, mmax)
                return node

        return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans