import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        flg = True
        while flg and dummy.next:
            flg = False
            prev = dummy
            curr = dummy.next
            while curr.next:
                nxt = curr.next
                if curr.val > nxt.val:
                    prev.next, curr.next, nxt.next = nxt, nxt.next, curr
                    prev = nxt
                    flg = True
                else:
                    prev, curr = curr, nxt
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        l1, l2, mid.next = head, mid.next, None
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.merge(l1, l2)

    def get_mid(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
                curr.next = None
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
                curr.next = None
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
