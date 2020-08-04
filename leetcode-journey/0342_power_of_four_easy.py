class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num > 1:
            if num % 4 != 0:
                return False
            num /= 4
        return True if num == 1 else False