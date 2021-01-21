from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


print(Solution().findKthLargest([2, 1], 2))



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stack = [float('inf')] + [float('-inf')] * (k + 1)
        for n in nums:
            stack[-1] = n
            cur = -1
            while stack[cur] > stack[cur - 1]:
                stack[cur], stack[cur - 1] = stack[cur - 1], stack[cur]
                cur -= 1
        return stack[-2]