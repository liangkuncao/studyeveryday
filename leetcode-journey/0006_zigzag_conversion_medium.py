class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        zigzag = [''] * numRows
        step, row = 1, 0
        for c in s:
            zigzag[row] += c
            row += step
            if row in (0, numRows - 1):
                step = -step
        return ''.join([row for row in zigzag])