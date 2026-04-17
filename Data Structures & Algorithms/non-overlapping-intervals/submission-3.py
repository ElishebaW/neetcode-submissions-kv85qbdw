class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
       
        res = 0
        prev_end = sorted_intervals[0][1]

        for s, e in sorted_intervals[1:]:
            if s < prev_end:
                res += 1
            else:
                prev_end = e

        return res

