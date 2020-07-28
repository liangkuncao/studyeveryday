class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        row_len, col_len = len(matrix), len(matrix[0])
        max_breadth = 0
        dp = [[0 for _ in range(col_len)] for _ in range(row_len)]
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == '1':
                    if row == 0 or col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1
                    max_breadth = max(max_breadth, dp[row][col])
        return max_breadth ** 2
