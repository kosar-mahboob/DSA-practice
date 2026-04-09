from typing import List
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
    
        
        # dp_max and dp_min will store the maximum and minimum product for each cell
        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]
        
        # Initialize top-left cell
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                # Candidates from top (i-1, j) and left (i, j-1)
                candidates = []
                if i > 0:
                    candidates.extend([dp_max[i-1][j] * grid[i][j], dp_min[i-1][j] * grid[i][j]])
                if j > 0:
                    candidates.extend([dp_max[i][j-1] * grid[i][j], dp_min[i][j-1] * grid[i][j]])
                # If no candidates (should not happen for non-start cells), but we handle anyway
                if not candidates:
                    continue
                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)
        
        final = dp_max[m-1][n-1]
        return final % MOD if final >= 0 else -1
