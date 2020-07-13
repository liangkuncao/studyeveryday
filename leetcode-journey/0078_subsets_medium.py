from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(nums: List[int], subset: List[int] = []):
            if not nums:
                res.append(subset)
                return
            helper(nums[1:], subset + [nums[0]])
            helper(nums[1:], subset)

        res = []
        helper(nums)
        return res


print(Solution().subsets([1, 2, 3]))