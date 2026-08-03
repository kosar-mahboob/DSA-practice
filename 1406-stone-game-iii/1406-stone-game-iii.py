class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)
        
        for i in range(n - 1, -1, -1):
            take1 = stoneValue[i] - dp[i + 1]
            take2 = stoneValue[i] + stoneValue[i + 1] - dp[i + 2] if i + 1 < n else float('-inf')
            take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3] if i + 2 < n else float('-inf')
            dp[i] = max(take1, take2, take3)
        
        if dp[0] > 0: return "Alice"
        if dp[0] < 0: return "Bob"
        return "Tie"