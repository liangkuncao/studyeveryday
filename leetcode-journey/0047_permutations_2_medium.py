class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def help(s_nums: List[int], cur: List[int]):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for i in range(len(s_nums)):
                if i > 0 and s_nums[i] == s_nums[i - 1]:
                    continue
                tmp = s_nums[:]
                cur.append(tmp.pop(i))
                help(tmp, cur)
                cur.pop()

        nums.sort()
        res = []
        help(nums, [])
        return res