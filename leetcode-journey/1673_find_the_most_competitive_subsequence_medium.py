class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, n in enumerate(nums):
            while stack and stack[-1] > n and len(nums) - i + len(stack) > k:
                stack.pop()
            if len(stack) < k:
                stack.append(n)
        return stack