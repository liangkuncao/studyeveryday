class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = [interval + [idx] for idx, interval in enumerate(intervals)]
        sorted_intervals = sorted(intervals, key=lambda i: i[0])

        res = []
        for interval in intervals:
            idx = float('inf')
            left, right = 0, len(intervals) - 1
            end = interval[1]
            while left <= right:
                mid = (left + right) // 2
                start = sorted_intervals[mid][0]
                orig_idx = sorted_intervals[mid][2]
                if start < end:
                    left = mid + 1
                elif start == end:
                    idx = orig_idx
                    break
                else:
                    idx = min(idx, orig_idx)
                    right = mid - 1
            res.append(-1 if idx == float('inf') else idx)
        return res