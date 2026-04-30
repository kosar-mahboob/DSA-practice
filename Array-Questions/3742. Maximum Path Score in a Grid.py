from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # Maximum possible cost from (0,0) to (m-1,n-1): each step adds at most 1 cost,
        # number of steps = (m-1)+(n-1) = m+n-2
        max_cost_possible = m + n - 2
        C = min(k, max_cost_possible)
        
        # prev[j][c] = max score at cell (i-1, j) with exact cost c, -1 = unreachable
        prev = [[-1] * (C + 1) for _ in range(n)]
        prev[0][0] = 0  # start at (0,0)
        
        for i in range(m):
            cur = [[-1] * (C + 1) for _ in range(n)]
            for j in range(n):
                val = grid[i][j]
                score_add = val
                cost_add = 1 if (val == 1 or val == 2) else 0
                
                # from top
                if i > 0:
                    for c in range(cost_add, C + 1):
                        if prev[j][c - cost_add] != -1:
                            new_score = prev[j][c - cost_add] + score_add
                            if new_score > cur[j][c]:
                                cur[j][c] = new_score
                # from left
                if j > 0:
                    for c in range(cost_add, C + 1):
                        if cur[j-1][c - cost_add] != -1:
                            new_score = cur[j-1][c - cost_add] + score_add
                            if new_score > cur[j][c]:
                                cur[j][c] = new_score
                # start cell
                if i == 0 and j == 0:
                    cur[0][0] = 0
            prev = cur
        
        ans = max(cur[n-1])
        return -1 if ans == -1 else ans
