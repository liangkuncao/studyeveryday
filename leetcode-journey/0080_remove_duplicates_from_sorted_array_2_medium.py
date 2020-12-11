class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = count = 0
        for i, val in enumerate(nums):
            if i > 0 and nums[i] != nums[i - 1]:
                count = 0
            if count < 2:
                count += 1
                nums[cur] = nums[i]
                cur += 1
        return cur

