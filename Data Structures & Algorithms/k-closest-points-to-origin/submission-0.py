class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closets_points = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(closets_points, (-dist, x, y))

            if len(closets_points) > k:
                heapq.heappop(closets_points)
        
        results = []
        for dist, x1, y1 in closets_points:
            results.append([x1, y1])

        return results

        
