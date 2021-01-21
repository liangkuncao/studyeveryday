class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        for i in range(len(s)):
            p = self.get_longest_palindrome(s, i, i)
            if len(p) > len(palindrome):
                palindrome = p

            p = self.get_longest_palindrome(s, i, i + 1)
            if len(p) > len(palindrome):
                palindrome = p
        return palindrome

    def get_longest_palindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        return s[j + 1: k]


print(Solution().longestPalindrome('cbbd'))

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        i = 0
        while i < len(s):
            if len(s)-i < len(res)//2:
                break
            h, j = i - 1, i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            i = j
            while h >= 0 and j < len(s) and s[h] == s[j]:
                h -= 1
                j += 1
            if j - h - 1 > len(res):
                res = s[h + 1: j]
        return res
