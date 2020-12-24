class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l
        left, right = 0, l - 1
        cur = l - 1
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                res[cur] = nums[right] ** 2
                right -= 1
            else:
                res[cur] = nums[left] ** 2
                left += 1
            cur -= 1
        return res



