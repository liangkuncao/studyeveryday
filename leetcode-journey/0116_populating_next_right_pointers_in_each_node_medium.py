"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur, head, prev = root, None, None
        while cur:
            if cur.left:
                if prev:
                    prev.next = cur.left
                else:
                    prev = cur.left
                    head = prev
                prev = cur.left
            if cur.right:
                if prev:
                    prev.next = cur.right
                else:
                    prev = cur.right
                    head = prev
                prev = cur.right
            cur = cur.next
            if not cur:
                cur, head, prev = head, None, None
        return root