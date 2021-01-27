class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res, bits = 0, 1
        for i in range(1, n + 1):
            res <<= bits
            res += i
            res %= (10**9 + 7)
            if i == (1 << bits) - 1:
                bits += 1
        return res
