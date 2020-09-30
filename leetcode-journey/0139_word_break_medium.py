class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                prev, curr = i - len(word), i
                if prev >= 0 and dp[prev] and s[prev:curr] == word:
                    dp[curr] = True
                    break
        return dp[-1]