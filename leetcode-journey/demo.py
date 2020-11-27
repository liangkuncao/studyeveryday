from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [True] + [False] * target
        for num in nums:
            for i in range(num, len(dp)):
                if 0 <= i - num <= len(dp) and dp[i - num]:
                    dp[i] = True
            if dp[target]:
                return True
        return False


print(Solution().canPartition([1,2,5]))