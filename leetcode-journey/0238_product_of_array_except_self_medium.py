class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        to_right = [1] * len(nums)
        for i in range(1, len(nums)):
            to_right[i] = to_right[i - 1] * nums[i - 1]
        to_left = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            to_left[i] = to_left[i + 1] * nums[i + 1]
        return [x * y for x, y in zip(to_right, to_left)]