# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            print(d1, d2)
            quotient, remainder = divmod(d1 + d2, 10)
            cur.next = ListNode(val=quotient + carry)
            carry = remainder
            cur, l1, l2 = cur.next, l1.next, l2.next
            print(cur.val)
        if carry:
            cur.next = ListNode(carry)
        return dummy.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(Solution().addTwoNumbers(l1, l2))