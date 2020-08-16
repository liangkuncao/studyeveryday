from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initial states
        sold = float('-inf')
        held = float('-inf')
        reset = 0
        for price in prices:
            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)
        return max(sold, reset)

print(Solution().maxProfit([1,2,3,0,2]))