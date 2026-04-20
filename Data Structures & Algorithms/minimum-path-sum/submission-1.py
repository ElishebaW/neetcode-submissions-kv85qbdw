class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        result = [[float("inf")] * N for _ in range(M)]
        result[M - 1][N -1] = grid[M - 1][N - 1]

        for i in range(M -1, -1 , -1):
            for j in range( N - 1, -1, -1):
                if i == M - 1 and j == N -1:
                    continue
                elif i == M -1:
                    result[i][j] = result[i][j + 1] + grid[i][j]
                elif  j == N - 1:
                    result[i][j] = result[i + 1][j] + grid[i][j]
                else:
                    result[i][j] = grid[i][j] + min(result[i + 1][j], result[i][j + 1])

        return result[0][0]