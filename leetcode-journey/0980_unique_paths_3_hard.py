class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        starting, ending = None, None
        empty = set()
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 0:
                    empty.add((r, c))
                elif cell == 1:
                    starting = (r, c)
                elif cell == 2:
                    ending = (r, c)
        empty.add(ending)

        res = self.helper(0, starting, empty, ending)
        return res

    def helper(self, count: int, curr: tuple, empty: Set[tuple], ending: tuple) -> int:
        if not empty:
            if curr == ending:
                count += 1
            return count

        left = (curr[0] - 1, curr[1])
        right = (curr[0] + 1, curr[1])
        up = (curr[0], curr[1] - 1)
        down = (curr[0], curr[1] + 1)
        nexts = [left, right, up, down]
        for i in nexts:
            if i in empty:
                empty.discard(i)
                count = self.helper(count, i, empty, ending)
                empty.add(i)
        return count