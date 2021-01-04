class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        small, large = 1, max(nums)
        res = 0
        while small <= large:
            mid = (small + large) // 2
            total = sum([ceil(num / mid) for num in nums])
            if total > threshold:
                small = mid + 1
            else:
                res = mid
                large = mid - 1
        return res