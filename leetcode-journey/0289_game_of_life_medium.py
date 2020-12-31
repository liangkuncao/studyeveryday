class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        for i in range(m):
            for j in range(n):
                live = 0
                for dx, dy in direction:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and board[x][y] & 1:
                        live += 1
                if board[i][j] == 0 and live == 3:
                        board[i][j] = 2
                elif board[i][j] == 1 and 2 <= live <= 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1