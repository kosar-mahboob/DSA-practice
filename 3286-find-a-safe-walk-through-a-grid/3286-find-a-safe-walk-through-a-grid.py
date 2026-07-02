from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # If starting cell is unsafe and health drops to 0, can't start
        initial_health = health - grid[0][0]
        if initial_health <= 0:
            return False
        
        # visited[r][c] = max health remaining when reaching (r,c)
        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = initial_health
        
        q = deque([(0, 0, initial_health)])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            r, c, h = q.popleft()
            
            if r == m - 1 and c == n - 1:
                return True
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_health = h - grid[nr][nc]
                    # Must have positive health after moving
                    if new_health > 0 and new_health > visited[nr][nc]:
                        visited[nr][nc] = new_health
                        q.append((nr, nc, new_health))
        
        return False