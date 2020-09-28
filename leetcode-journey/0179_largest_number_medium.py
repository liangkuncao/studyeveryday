import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums = sorted(nums, reverse=True, key=Compare)
        return '0' if nums[0] == '0' else ''.join(nums)


class Compare(str):
    def __lt__(x, y):
        return x + y < y + x