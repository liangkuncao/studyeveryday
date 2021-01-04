# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        while head and head.next:
            if head.val > head.next.val:
                target = head.next
                prev = dummy
                while prev.next.val < target.val:
                    prev = prev.next
                temp = prev.next
                prev.next = target
                head.next = target.next
                target.next = temp
            else:
                head = head.next
        return dummy.next

