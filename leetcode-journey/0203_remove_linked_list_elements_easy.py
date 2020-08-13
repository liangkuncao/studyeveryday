# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, dummy.next
        while curr:
            while curr and curr.val == val:
                curr = curr.next
            prev.next = curr
            prev = curr
            curr = curr.next if curr else None
        return dummy.next