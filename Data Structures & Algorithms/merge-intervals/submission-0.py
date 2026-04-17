class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        queue = deque([sorted_intervals[0]])

        for interval in sorted_intervals[1:]:
            current_interval = queue[-1]
            current_start = current_interval[0]
            current_end = current_interval[1]
            next_start = interval[0]
            next_end = interval[1]

            if current_end >= next_start:
                current_interval[1] = max(current_interval[1], interval[1])
            else:
                queue.append(interval)

        return list(queue)