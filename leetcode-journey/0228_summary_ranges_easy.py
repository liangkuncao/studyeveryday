class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        for i in range(len(nums)):
            if not res or nums[i] - res[-1][1] > 1:
                res.append([nums[i], nums[i]])
            else:
                res[-1][1] = nums[i]
        for idx, r in enumerate(res):
            if r[0] == r[1]:
                res[idx] = str(r[0])
            else:
                res[idx] = str(r[0]) + '->' + str(r[1])
        return res