# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode()
        dummy.next = head
        while cur and cur.next and cur.next.next:
            first, second = cur.next, cur.next.next
            cur.next, first.next, second.next = second, second.next, first
            cur = first
        return dummy.next