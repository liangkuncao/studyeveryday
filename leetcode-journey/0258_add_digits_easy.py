class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sum_ = 0
            while num > 0:
                remainder, num = num % 10, num // 10
                sum_ += remainder
            num = sum_
        return num