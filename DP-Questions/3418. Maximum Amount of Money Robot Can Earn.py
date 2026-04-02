from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        INF_NEG = -10**18
        # dp[i][j][k] = max coins at (i,j) having used k neutralizations (0,1,2)
        dp = [[[INF_NEG] * 3 for _ in range(n)] for _ in range(m)]

        # Starting cell
        val = coins[0][0]
        if val >= 0:
            dp[0][0][0] = val
            # cannot have used a neutralization if no robber
            dp[0][0][1] = INF_NEG
            dp[0][0][2] = INF_NEG
        else:
            dp[0][0][0] = val          # not neutralize
            dp[0][0][1] = 0            # neutralize
            dp[0][0][2] = INF_NEG      # cannot use two

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = coins[i][j]
                for k in range(3):
                    best = INF_NEG
                    # from above
                    if i > 0:
                        # not neutralize this cell
                        best = max(best, dp[i-1][j][k] + (val if val >= 0 else val))
                        # neutralize this cell (only if val < 0 and we have a neutralization left)
                        if k > 0 and val < 0:
                            best = max(best, dp[i-1][j][k-1] + 0)
                    # from left
                    if j > 0:
                        best = max(best, dp[i][j-1][k] + (val if val >= 0 else val))
                        if k > 0 and val < 0:
                            best = max(best, dp[i][j-1][k-1] + 0)
                    dp[i][j][k] = best

        return max(dp[m-1][n-1])
