from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:

        def dfs(nums: List[int], cur: int) -> None:
            if cur == 0:
                nonlocal res
                res += 1
                return
            for i in range(cur, 0, -1):
                nums[cur], nums[i] = nums[i], nums[cur]
                if nums[cur] % cur == 0 or cur % nums[cur] == 0:
                    dfs(nums, cur - 1)
                nums[cur], nums[i] = nums[i], nums[cur]

        res = 0
        dfs(list(range(n + 1)), n)
        return res