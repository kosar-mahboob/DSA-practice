from typing import List
import sys

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        sys.setrecursionlimit(m * n + 10)

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            val = grid[r][c]
            grid[r][c] = 0  # mark visited
            total = val
            total += dfs(r + 1, c)
            total += dfs(r - 1, c)
            total += dfs(r, c + 1)
            total += dfs(r, c - 1)
            return total

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if dfs(i, j) % k == 0:
                        count += 1
        return count