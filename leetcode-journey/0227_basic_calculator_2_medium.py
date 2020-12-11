class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        res = prev = 0
        idx = 0
        cur_operator = '+'
        while idx < len(s):
            cur = 0
            while idx < len(s) and s[idx].isdigit():
                cur = cur*10 + int(s[idx])
                idx += 1
            if cur_operator == '+':
                res += prev
                prev = cur
            elif cur_operator == '-':
                res += prev
                prev = -cur
            elif cur_operator == '*':
                prev *= cur
            else:
                prev = int(prev / cur)
            if idx < len(s) - 1:
                cur_operator = s[idx]
            idx += 1
        return res + prev