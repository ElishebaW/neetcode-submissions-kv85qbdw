class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n , m = len(heights), len(heights[0])
        pacific_border = set()
        atlantic_border = set()

        for r in range(n):
            pacific_border.add((r, 0))
            atlantic_border.add((r, m - 1))

        for c in range(m):
            pacific_border.add((0, c))
            atlantic_border.add((n - 1, c))

        def dfs(r, c, visited, prev_height):
            if r < 0 or r >= n or c < 0 or c >=m or (r,c) in visited or heights[r][c] < prev_height:
                return 
            
            visited.add((r,c))

            directions = [[0,1], [1,0], [-1,0],[0,-1]]

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        pacific = set()
        atlantic = set()
        for r, c in pacific_border:
            dfs(r, c, pacific, heights[r][c])

        for r, c in atlantic_border:
            dfs(r, c, atlantic, heights[r][c])

        return [[r,c] for r,c in pacific & atlantic]


        
        