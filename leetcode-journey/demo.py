from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals1 = []
        intervals2 = []

        for idx, interval in enumerate(intervals):
            left, right = interval[0], interval[1]
            if newInterval[0] < left:
                intervals1 = intervals[:idx]
                intervals1.append(newInterval)
                break
            elif left <= newInterval[0] <= right:
                intervals1 = intervals[:idx + 1]
                break

        for idx, interval in enumerate(intervals[::-1]):
            left, right = interval[0], interval[1]
            if newInterval[1] > right:
                intervals2 = intervals[len(intervals) - idx:]
                intervals2.insert(0, newInterval)
                break
            elif left <= newInterval[1] <= right:
                intervals2 = intervals[len(intervals) - 1 - idx:]
                break

        intervals1[-1][1] = intervals2.pop(0)[1]
        return intervals1 + intervals2


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(Solution().insert(intervals, newInterval))