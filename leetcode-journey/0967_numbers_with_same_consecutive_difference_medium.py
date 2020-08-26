class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        def dfs(num: int, remaining: int):
            if not remaining:
                res.append(num)
                return
            last_digit = num % 10
            if last_digit - K in range(10):
                dfs(num * 10 + (last_digit - K), remaining - 1)
            if last_digit + K != last_digit - K and last_digit + K in range(10):
                dfs(num * 10 + (last_digit + K), remaining - 1)

        res = []
        if N == 1:
            res.append(0)
        for i in range(1, 10):
            dfs(i, N - 1)
        return res