# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = [], []
        while l1:
            n1.append(l1.val)
            l1 = l1.next
        while l2:
            n2.append(l2.val)
            l2 = l2.next
        dummy = ListNode(-1)
        dummy.next = ListNode(0)
        while len(n1) > 0 or len(n2) > 0:
            curr = dummy.next
            if len(n1) > 0:
                curr.val += n1.pop()
            if len(n2) > 0:
                curr.val += n2.pop()
            new = ListNode(curr.val // 10)
            curr.val %= 10
            dummy.next, new.next = new, curr
        return dummy.next if dummy.next.val > 0 else dummy.next.next