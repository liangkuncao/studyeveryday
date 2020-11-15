class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left, left_count = 0, 0
        while left < len(seats):
            if seats[left] == 0:
                left_count += 1
                left += 1
            else:
                break
        right, right_count = len(seats) - 1, 0
        while right >= 0:
            if seats[right] == 0:
                right_count += 1
                right -= 1
            else:
                break
        mid_count = 0
        tmp = 0
        for i in range(left, right + 1):
            if seats[i] == 0:
                tmp += 1
            else:
                mid_count = max(mid_count, tmp)
                tmp = 0
        return max(left_count, (mid_count + 1) // 2, right_count)