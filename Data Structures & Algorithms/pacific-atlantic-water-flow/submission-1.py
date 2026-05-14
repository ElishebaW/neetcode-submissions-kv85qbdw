class Solution:
    def pacificAtlantic(self, heights):
        n, m = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if r < 0 or r >= n or c < 0 or c >= m or (r,c) in visited or heights[r][c] < prev_height:
                return
            visited.add((r, c))
            for dr, dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                dfs(r+dr, c+dc, visited, heights[r][c])

        for r in range(n):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, m-1, atlantic, heights[r][m-1])

        for c in range(m):
            dfs(0, c, pacific, heights[0][c])
            dfs(n-1, c, atlantic, heights[n-1][c])

        return [[r, c] for r, c in pacific & atlantic]

        
        