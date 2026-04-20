class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        for i in range(M -1, -1 , -1):
            for j in range( N - 1, -1, -1):
                if i == M - 1 and j == N -1:
                    continue
                elif i == M -1:
                   grid[i][j] = grid[i][j + 1] + grid[i][j]
                elif  j == N - 1:
                    grid[i][j] = grid[i + 1][j] + grid[i][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i + 1][j], grid[i][j + 1])

        return grid[0][0]