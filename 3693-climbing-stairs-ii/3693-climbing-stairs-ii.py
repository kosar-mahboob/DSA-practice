class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue
            for j in range(i + 1, min(i + 4, n + 1)):
                cost = costs[j - 1] + (j - i) ** 2
                if dp[i] + cost < dp[j]:
                    dp[j] = dp[i] + cost

        return dp[n]
