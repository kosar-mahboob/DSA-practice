from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    stack = [(i, j, -1, -1)]
                    visited[i][j] = True
                    
                    while stack:
                        r, c, pr, pc = stack.pop()
                        for dr, dc in dirs:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == grid[i][j]:
                                if (nr, nc) == (pr, pc):
                                    continue
                                if visited[nr][nc]:
                                    return True
                                visited[nr][nc] = True
                                stack.append((nr, nc, r, c))
        return False
