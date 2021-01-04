class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = [0] * 26
        for c in s:
            letters[ord(c) - ord('a')] += 1
        for c in t:
            letters[ord(c) - ord('a')] -= 1
            if letters[ord(c) - ord('a')] < 0:
                return c
