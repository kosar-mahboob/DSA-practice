class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        isPal = [[False] * n for _ in range(n)]
        for i in range(n):
            isPal[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i+1]:
                isPal[i][i+1] = True
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and isPal[i+1][j-1]:
                    isPal[i][j] = True
        
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1]
            for j in range(i - k + 1):
                if isPal[j][i-1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[n]