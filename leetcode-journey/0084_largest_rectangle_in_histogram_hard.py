class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [-1] + heights + [-1]
        res = 0
        stack = []
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                last = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[last])
            stack.append(i)
        return res