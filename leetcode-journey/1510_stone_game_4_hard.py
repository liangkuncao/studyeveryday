class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(n + 1):
            if dp[i]:
                continue
            for j in range(1, int(n ** 0.5) + 1):
                if i + j ** 2 <= n:
                    dp[i + j ** 2] = True
                else:
                    break
        return dp[n]