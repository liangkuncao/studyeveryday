class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        directions = ((0, 1), (1, -1), (1, 0), (-1, 1))
        cur_dir = 3
        x, y = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        res.append(matrix[x][y])
        while True:
            if x == rows - 1 and y == cols - 1:
                break
            nxt_x, nxt_y = x + directions[cur_dir][0], y + directions[cur_dir][1]
            if not 0 <= nxt_x < rows or not 0 <= nxt_y < cols:
                cur_dir = cur_dir + 1 if cur_dir < 3 else 0
                nxt_x, nxt_y = x + directions[cur_dir][0], y + directions[cur_dir][1]
            if nxt_y == cols:
                nxt_x, nxt_y = x + directions[2][0], y + directions[2][1]
            if nxt_x == rows:
                nxt_x, nxt_y = x + directions[0][0], y + directions[0][1]
            x, y = nxt_x, nxt_y
            res.append(matrix[x][y])
            if cur_dir == 0 or cur_dir == 2:
                cur_dir = cur_dir + 1 if cur_dir < 3 else 0
        return res