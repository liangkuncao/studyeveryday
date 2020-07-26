# can't process negative number
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1

        negative = (dividend > 0) ^ (divisor > 0)
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor
        result = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift += 1
            dividend -= divisor << (shift - 1)
            result += 1 << (shift - 1)
        return -result if negative else result