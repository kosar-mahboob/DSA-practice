from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ')':
            return False

        # dp[i][j] = set of possible balances at cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                rem = (m - 1 - i) + (n - 1 - j)  # remaining steps to end
                bal = set()
                if i > 0:
                    for b in dp[i - 1][j]:
                        nb = b + 1 if grid[i][j] == '(' else b - 1
                        if 0 <= nb <= rem:
                            bal.add(nb)
                if j > 0:
                    for b in dp[i][j - 1]:
                        nb = b + 1 if grid[i][j] == '(' else b - 1
                        if 0 <= nb <= rem:
                            bal.add(nb)
                dp[i][j] = bal

        return 0 in dp[m - 1][n - 1]