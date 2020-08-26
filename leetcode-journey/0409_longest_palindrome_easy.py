from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        num_odd = 0
        letters = defaultdict(int)
        for char in s:
            if letters[char]:
                letters[char] -= 1
                num_odd -= 1
                res += 2
            else:
                letters[char] += 1
                num_odd += 1
        return res + 1 if num_odd else res

