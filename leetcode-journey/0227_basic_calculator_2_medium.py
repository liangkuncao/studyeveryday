class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        res = 0
        prev = 0
        sign = '+'
        i = 0
        while i < len(s):
            curr = 0
            while i < len(s) and ord('0') <= ord(s[i]) <= ord('9'):
                curr = curr * 10 + (ord(s[i]) - ord('0'))
                i += 1
            if sign == '+':
                res += prev
                prev = curr
            elif sign == '-':
                res += prev
                prev = -curr
            elif sign == '*':
                prev *= curr
            elif sign == '/':
                prev = int(prev / curr)
            if i + 1 < len(s):
                sign = s[i]
            i += 1
        return res + prev



