from typing import List
from collections import defaultdict


class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n + 1)]

        def dfs(nums: List[int], cur: List[int]) -> None:
            nonlocal res
            if len(nums) == 0:
                if is_beautiful(cur):
                    res += 1
            for i, n in enumerate(nums):
                cur.append(n)
                dfs(nums[:i] + nums[i + 1:], cur)
                cur.pop()

        def is_beautiful(nums: List[int]) -> bool:
            for i, n in enumerate(nums):
                j = i + 1
                if j % n == 0 or n % j == 0:
                    continue
                else:
                    return False
            return True

        res = 0
        dfs(nums, [])
        return res


print(Solution().countArrangement(3))