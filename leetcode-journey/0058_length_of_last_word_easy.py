class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        end = n
        start = 0
        for i in range(n - 1, -1, -1):
            if s[i] != ' ':
                end = i + 1
                break
        for i in range(end - 1, -1, -1):
            if s[i] == ' ':
                start = i + 1
                break
        return end - start