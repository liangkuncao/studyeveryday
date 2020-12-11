class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        seen = set()
        remainder = 1
        length = 1
        while remainder%K != 0:
            num = remainder*10 + 1
            remainder = num % K
            length += 1
            if remainder in seen:
                return -1
            else:
                seen.add(remainder)
        return length