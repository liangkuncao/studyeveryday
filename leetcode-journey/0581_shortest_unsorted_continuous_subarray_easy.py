class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # monotonic stack
        stack = []
        left_bound, right_bound = len(nums) - 1, 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                left_bound = min(left_bound, stack.pop())
            stack.append(i)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right_bound = max(right_bound, stack.pop())
            stack.append(i)
        return right_bound - left_bound + 1 if right_bound > left_bound else 0