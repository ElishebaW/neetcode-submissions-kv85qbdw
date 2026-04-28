class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False

        for interval in intervals:
            if inserted:
                result.append(interval)
                continue

            s = interval[0]
            e = interval[1]
            ns = newInterval[0]
            ne = newInterval[1]
            if ne < s:
                inserted = True
                result.append(newInterval)
                result.append(interval)
            elif e < ns:
                result.append(interval)
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        if not inserted:
            result.append(newInterval)
        
        return result

        