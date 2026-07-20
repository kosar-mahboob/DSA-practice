class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total  # Reduce k to avoid unnecessary shifts
        
        # Flatten the grid
        flat = []
        for row in grid:
            flat.extend(row)
        
        # Rotate right by k positions
        flat = flat[-k:] + flat[:-k] if k else flat
        
        # Reshape back to 2D
        result = []
        for i in range(m):
            result.append(flat[i * n : (i + 1) * n])
        
        return result