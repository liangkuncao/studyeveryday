class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # monotonic stack
        left_bound, right_bound = len(nums) - 1, 0

        asc_stack = []
        i = 0
        while i < len(nums):
            if len(asc_stack) == 0 or nums[i] >= nums[asc_stack[-1]]:
                asc_stack.append(i)
            else:
                left_bound = min(left_bound, asc_stack.pop())
                i -= 1
            i += 1

        desc_stack = []
        j = len(nums) - 1
        while j >= 0:
            if len(desc_stack) == 0 or nums[j] <= nums[desc_stack[-1]]:
                desc_stack.append(j)
            else:
                right_bound = max(right_bound, desc_stack.pop())
                j += 1
            j -= 1

        return right_bound - left_bound + 1 if right_bound - left_bound > 0 else 0