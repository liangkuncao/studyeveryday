class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min1, min2, max1, max2 = float('inf'), float('inf'), float('-inf'), float('-inf')
        for n in nums:
            n -= 1
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
        return max(min1 * min2, max1 * max2)