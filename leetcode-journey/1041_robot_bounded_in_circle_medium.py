class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
        idx = 0
        d = ds[idx]
        for c in instructions:
            if c == 'G':
                x, y = x + d[0], y + d[1]
            elif c == 'L':
                idx = idx - 1 if idx > 0 else 3
                d = ds[idx]
            else:
                idx = idx + 1 if idx < 3 else 0
                d = ds[idx]
        return (x == 0 and y == 0) or idx != 0
