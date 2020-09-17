class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [0, 1, 2, 3]
        curr_dir, init_dir = 0, 0
        curr_pos, init_pos = [0, 0], [0, 0]
        for i in instructions:
            if i == 'L':
                curr_dir = directions[curr_dir - 1]
            elif i == 'R':
                curr_dir = directions[(curr_dir + 1) % 4]
            elif i == 'G':
                if curr_dir == 0:
                    curr_pos[1] += 1
                elif curr_dir == 1:
                    curr_pos[0] += 1
                elif curr_dir == 2:
                    curr_pos[1] -= 1
                elif curr_dir == 3:
                    curr_pos[0] -= 1
        return curr_dir != init_dir or curr_pos == init_pos


print(Solution().isRobotBounded("GG"))