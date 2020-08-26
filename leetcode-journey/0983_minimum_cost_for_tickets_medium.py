class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        first, last = days[0], days[-1]
        days = set(days)
        dp = [0] * (last + 1)
        for i in range(first, last + 1):
            if i in days:
                p1 = dp[i - 1] if i - 1 > 0 else 0
                p2 = dp[i - 7] if i - 7 > 0 else 0
                p3 = dp[i - 30] if i - 30 > 0 else 0
                dp[i] = min(p1 + costs[0], p2 + costs[1], p3 + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[-1]