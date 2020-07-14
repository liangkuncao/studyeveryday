class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        elif num < 1:
            return False

        for i in [2, 3, 5]:
            while num % i == 0:
                num //= i
        return num == 1