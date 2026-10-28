class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        for j in range(1, n):
            for v in dp[j-1]:
                dp[j].add(v ^ grid[0][j])
        for i in range(1, m):
            dp[0] = {v ^ grid[i][0] for v in dp[0]}
            for j in range(1, n):
                vals = set()
                for v in dp[j]:
                    vals.add(v ^ grid[i][j])
                for v in dp[j-1]:
                    vals.add(v ^ grid[i][j])
                dp[j] = vals
        return min(dp[n-1])