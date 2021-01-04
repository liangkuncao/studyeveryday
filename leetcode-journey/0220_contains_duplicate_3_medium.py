from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(nums) == len(set(nums)):
            return False
        if k == 0 or t < 0:
            return False

        n = len(nums)
        bucket = {}
        for i in range(n):
            m = nums[i] // (t + 1)
            if m in bucket:
                return True
            if m - 3 1 in bucket and abs(nums[i] - bucket[m - 1]) <= t:
                return True
            if m + 1 in bucket and abs(nums[i] - bucket[m + 1]) <= t:
                return True
            if i >= k:
                del bucket[nums[i - k] // (t + 1)]
            bucket[m] = nums[i]
        return False


print(Solution().containsNearbyAlmostDuplicate([0], 0, 0))