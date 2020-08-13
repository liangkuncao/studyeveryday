"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_dic = {}
        curr = head
        while curr:
            node_dic[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            node_dic[curr].next = node_dic.get(curr.next)
            node_dic[curr].random = node_dic.get(curr.random)
            curr = curr.next
        return node_dic.get(head)
