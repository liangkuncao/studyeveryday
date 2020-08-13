class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        queue = list()
        num_fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        if not num_fresh:
            return 0

        while queue and num_fresh:
            minutes += 1
            new_rottens = list()
            for i, j in queue:
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    new_rottens.append((i, j - 1))
                    num_fresh -= 1
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    new_rottens.append((i - 1, j))
                    num_fresh -= 1
                if j + 1 < cols and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    new_rottens.append((i, j + 1))
                    num_fresh -= 1
                if i + 1 < rows and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    new_rottens.append((i + 1, j))
                    num_fresh -= 1
            queue = new_rottens

        return -1 if num_fresh else minutes