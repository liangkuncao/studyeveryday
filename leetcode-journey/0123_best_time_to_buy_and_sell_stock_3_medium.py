class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        N = len(prices)

        min_price = prices[0]
        profits1 = [0] * N
        for i in range(1, N):
            min_price = prices[i] if prices[i] < min_price else min_price
            profits1[i] = max(profits1[i - 1], prices[i] - min_price)

        max_price = prices[-1]
        profits2 = [0] * N
        for i in range(N - 2, -1, -1):
            max_price = prices[i] if prices[i] > max_price else max_price
            profits2[i] = max(profits2[i + 1], max_price - prices[i])

        optimum = 0
        for p1, p2 in zip(profits1, profits2):
            optimum = max(optimum, p1 + p2)
        return optimum