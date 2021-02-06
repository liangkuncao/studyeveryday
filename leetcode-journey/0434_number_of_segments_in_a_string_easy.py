class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        s += ' '
        for i, c in enumerate(s):
            if i > 0 and c == ' ' and s[i - 1] != ' ':
                res += 1
        return res