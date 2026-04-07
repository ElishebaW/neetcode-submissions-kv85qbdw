class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Create a 2d array for dp to store the path so far
        then iterates through the grid
        if in bounds than do. grid[i][j] + min(dp[i- 1][j], dp[i][j-1])
        if j - 1 outside of bounds = 0
        if i-1 outside of bounds = 0

        return dp[0]


        [1,2,0],[1 , 3 , 3]
        [5,4,2],[6 , 7,5]
        [1,1,3] [7 , 8, 8]
        """

        ROWS, COLS = len(grid), len(grid[0])
        res = [[float("inf")] * ( COLS + 1) for r in range(ROWS + 1)]

        res[ROWS - 1][COLS] = 0

        for r in range(ROWS - 1, -1 , -1):
            for c in range(COLS - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c+1])

        return res[0][0]