class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # dp[i][M] = max stones current player can get from i to end, with current M
        dp = [[0] * (n + 1) for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                max_stones = 0
                for X in range(1, min(2 * M, n - i) + 1):
                    taken = suffix_sum[i] - suffix_sum[i + X]
                    # After taking X piles, next player starts at i+X with new M = max(M, X)
                    next_M = max(M, X)
                    # Next player's optimal gain from the rest
                    opponent_gain = dp[i + X][next_M] if i + X < n else 0
                    # Our total gain = taken + (remaining stones - opponent_gain)
                    max_stones = max(max_stones, taken + (suffix_sum[i + X] - opponent_gain))
                dp[i][M] = max_stones

        return dp[0][1]