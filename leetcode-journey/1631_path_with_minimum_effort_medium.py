class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        effortdic = defaultdict(lambda: float('inf'))
        queue = [(0, 0, 0)]
        while queue:
            effort, curx, cury = heappop(queue)
            if curx == rows - 1 and cury == cols - 1:
                return effort
            for dx, dy in dirs:
                tx, ty = curx + dx, cury + dy
                if 0 <= tx < rows and 0 <= ty < cols:
                    tmp = max(effort, abs(heights[tx][ty] - heights[curx][cury]))
                    if tmp < effortdic[(tx, ty)]:
                        effortdic[(tx, ty)] = tmp
                        heappush(queue, (tmp, tx, ty))
