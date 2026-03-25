from typing import List

class Solution:
    def equalSumGridPartition(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        if total % 2 != 0:
            return False
        target = total // 2
        
        # Check horizontal cuts
        row_sum = 0
        for i in range(m):
            row_sum += sum(grid[i])
            if row_sum == target and i < m - 1:
                return True
        
        # Check vertical cuts
        col_sum = 0
        for j in range(n):
            col_sum += sum(grid[i][j] for i in range(m))
            if col_sum == target and j < n - 1:
                return True
        
        return False
