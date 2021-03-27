from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def help(cur: int, remain: int):
            for c in coins:
                if remain < c:
                    continue
                elif remain == c:
                    return cur + 1
                else:
                    res = help(cur + 1, remain - c)
                    if res:
                        return res

        if amount == 0:
            return 0
        coins.sort(reverse=True)
        res = help(0, amount)
        return res if res else -1


res = Solution().coinChange([186,419,83,408], 6249)
print(res)