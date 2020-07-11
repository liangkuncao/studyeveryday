class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for idx, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                res[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)
        return res