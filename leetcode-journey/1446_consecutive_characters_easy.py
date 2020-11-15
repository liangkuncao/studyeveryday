class Solution:
    def maxPower(self, s: str) -> int:
        res = 0
        curr, count = '', 0
        for ch in s:
            if ch == curr:
                count += 1
            else:
                res = max(res, count)
                curr, count = ch, 1
        res = max(res, count)
        return res