class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        r, c = 0, col - 1
        while r < row and c >= 0:
            curr = matrix[r][c]
            if target == curr:
                return True
            elif target < curr:
                c -= 1
            else:
                r += 1
        return False