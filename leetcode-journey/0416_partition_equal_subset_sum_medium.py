class Solution:
    def canPartition(self, nums):
        if len(nums) < 2:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]
            if dp[target]:
                return True
        return False