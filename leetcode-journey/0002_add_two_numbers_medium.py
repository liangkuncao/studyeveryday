# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            carry, remainder = divmod(d1 + d2 + carry, 10)
            cur.next = ListNode(remainder)
            cur, l1, l2 = cur.next, l1.next if l1 else None, l2.next if l2 else None
        if carry:
            cur.next = ListNode(carry)
        return dummy.next