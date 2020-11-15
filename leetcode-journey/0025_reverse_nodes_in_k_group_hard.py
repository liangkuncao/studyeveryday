# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while True:
            bucket = [None] * k
            node = prev.next
            for i in range(len(bucket)):
                if not node:
                    break
                bucket[i] = node
                node = node.next
            if not bucket[-1]:
                break
            self.reverse(bucket)
            prev.next = bucket[-1]
            prev = bucket[0]
        return dummy.next

    def reverse(self, bucket: List[ListNode]) -> None:
        bucket[0].next = bucket[-1].next
        for i in range(len(bucket) - 1, 0, -1):
            bucket[i].next = bucket[i - 1]