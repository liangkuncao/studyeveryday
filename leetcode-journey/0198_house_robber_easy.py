class Solution:
    def rob(self, nums: List[int]) -> int:
        pre2, pre1 = 0, 0
        curr = 0
        for num in nums:
            curr = max(num + pre2, pre1)
            pre2, pre1 = pre1, curr
        return curr