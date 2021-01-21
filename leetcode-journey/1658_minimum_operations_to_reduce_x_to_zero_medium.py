class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        res = float('inf')
        r = 0
        map_r = {}
        for i, n in enumerate([0] + nums):
            r += n
            map_r[r] = i
        for i , n in enumerate([0] + list(reversed(nums))):
            x -= n
            if x in map_r and map_r[x] + i <= len(nums):
                res = min(res, map_r[x] + i)
        return res if res < float('inf') else -1