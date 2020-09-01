class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        len_low, len_high = len(str(low)), len(str(high))
        digits = '123456789'
        for i in range(len_low, len_high + 1):
            for j in range(len(digits) - i + 1):
                if low <= int(digits[j:j+i]) <= high:
                    res.append(int(digits[j:j+i]))
        return res