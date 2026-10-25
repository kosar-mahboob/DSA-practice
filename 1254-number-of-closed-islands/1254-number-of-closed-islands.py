from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 0:
                return
            grid[r][c] = 1  # mark visited
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # Remove islands touching the border
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        # Count remaining islands
        count = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        
        return count