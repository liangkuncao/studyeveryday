class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ct = Counter(nums)
        res = 0
        if k == 0:
            for v in ct.values():
                res += v > 1
        else:
            for n in ct:
                res += (n + k) in ct
        return res