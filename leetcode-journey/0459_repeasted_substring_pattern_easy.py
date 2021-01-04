class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            times, remainder = divmod(len(s), i)
            if remainder:
                continue
            substr = s[:i]
            if substr * times == s:
                return True
        return False
