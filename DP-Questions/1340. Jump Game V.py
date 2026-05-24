from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n
        # Process indices from smallest value to largest (so dependencies are computed first)
        for i in sorted(range(n), key=lambda i: arr[i]):
            # Check jumps to the left
            for step in range(1, d + 1):
                j = i - step
                if j < 0:
                    break
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + dp[j])
            # Check jumps to the right
            for step in range(1, d + 1):
                j = i + step
                if j >= n:
                    break
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
