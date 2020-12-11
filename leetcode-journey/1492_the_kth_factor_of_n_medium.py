class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                k -= 1
                factors.append(n // i)
            if k == 0:
                return i
        if factors[-1] ** 2 == n:
            factors.pop()
        return -1 if k > len(factors) else factors[-k]