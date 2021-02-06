# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            middle = (left + right) // 2
            res = guess(middle)
            if res == -1:
                right = middle - 1
            elif res == 0:
                return middle
            elif res == 1:
                left = middle + 1