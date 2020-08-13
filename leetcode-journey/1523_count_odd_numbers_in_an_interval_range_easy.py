class Solution:
    def countOdds(self, low: int, high: int) -> int:
        range_ = high - low + 1
        res = range_ // 2
        if low % 2 == 1 and range_ % 2 == 1:
            res += 1
        return res