from typing import List
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # directions: 0: left, 1: right, 2: up, 3: down
        # For each street type, which directions it connects to
        # Street 1: left & right
        # Street 2: up & down
        # Street 3: left & down
        # Street 4: right & down
        # Street 5: left & up
        # Street 6: right & up
        dirs = {
            1: [0, 1],
            2: [2, 3],
            3: [0, 3],
            4: [1, 3],
            5: [0, 2],
            6: [1, 2]
        }
        
        # offsets: left, right, up, down
        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]
        # opposite direction indices
        opp = [1, 0, 3, 2]  # right, left, down, up
        
        visited = [[False] * n for _ in range(m)]
        q = deque()
        q.append((0, 0))
        visited[0][0] = True
        
        while q:
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return True
            cur = grid[r][c]
            for d in dirs[cur]:
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    nxt = grid[nr][nc]
                    # Check if the neighbour has the opposite direction
                    if opp[d] in dirs[nxt]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
        return False
