class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 1:
            return 0
        elif n < 2:
            return 1
        nums = [0] * (n + 1)
        nums[0], nums[1] = 0, 1
        res = float('-inf')
        for i in range(2, len(nums)):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i//2 + 1]
            res = max(res, nums[i])
        return res