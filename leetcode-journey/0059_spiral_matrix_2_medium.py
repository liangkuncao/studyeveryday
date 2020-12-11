class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        cur_x, cur_y = 0, -1
        cur_d = 0
        for i in range(1, n ** 2 + 1):
            cur_x += directions[cur_d][0]
            cur_y += directions[cur_d][1]
            res[cur_x][cur_y] = i

            nxt_x = cur_x + directions[cur_d][0]
            nxt_y = cur_y + directions[cur_d][1]
            if nxt_x < 0 or nxt_x >= n or nxt_y < 0 or nxt_y >= n or res[nxt_x][nxt_y]:
                cur_d = (cur_d + 1) % 4
        return res