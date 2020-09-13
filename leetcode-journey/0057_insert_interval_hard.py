class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        n = len(intervals)
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            i += 1
        res.extend(intervals[:i])
        l, r = newInterval[0], newInterval[1]
        while i < n and intervals[i][0] <= newInterval[1]:
            l = min(l, intervals[i][0])
            r = max(r, intervals[i][1])
            i += 1
        res.append([l, r])
        res.extend(intervals[i:])
        return res