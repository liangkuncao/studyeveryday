class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        res = 0
        last = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[last][1]:
                res += 1
                continue
            last = i
        return res