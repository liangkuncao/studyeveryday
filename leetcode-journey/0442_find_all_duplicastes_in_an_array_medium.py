class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = list()
        for idx, num in enumerate(nums):
            if num < 0:
                num = -num
            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return res