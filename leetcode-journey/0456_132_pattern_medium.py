class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        mins = [None] * len(nums)
        mins[0] = nums[0]
        for i in range(1, len(nums)):
            mins[i] = min(mins[i - 1], nums[i])
        stack = [nums[-1]]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i] > mins[i]:
                while stack and stack[-1] <= mins[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False
