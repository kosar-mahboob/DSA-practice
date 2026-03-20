from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows_out = m - k + 1
        cols_out = n - k + 1
        ans = [[0] * cols_out for _ in range(rows_out)]
        
        for i in range(rows_out):
            for j in range(cols_out):
                vals = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.add(grid[x][y])
                if len(vals) <= 1:
                    ans[i][j] = 0
                else:
                    sorted_vals = sorted(vals)
                    min_diff = float('inf')
                    for p in range(1, len(sorted_vals)):
                        diff = sorted_vals[p] - sorted_vals[p-1]
                        if diff < min_diff:
                            min_diff = diff
                    ans[i][j] = min_diff
        return ans
