class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1
        while 0 <= r < rows and 0 <= c < cols:
            curr = matrix[r][c]
            if curr == target:
                return True
            elif curr < target:
                r += 1
            else:
                c -= 1
        return False
