class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # Compute prefix sums in place
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]

        
        # Count valid submatrices
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] <= k:
                    count += 1
        return count
