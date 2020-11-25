from typing import List


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        num = 1
        length = 1
        while num % K != 0 and num <= 2 ** 63:
            num = num * 10 + 1
            length += 1
        return length if num <= 2 ** 63 else -1


print(Solution().smallestRepunitDivByK(1))
print(Solution().smallestRepunitDivByK(2))
print(Solution().smallestRepunitDivByK(3))

print(2 ** 63)