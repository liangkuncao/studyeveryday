class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = float('-inf')
        for i, n in enumerate(nums):
            if n == 1:
                if i - last - 1 >= k:
                    last = i
                else:
                    return False
        return True