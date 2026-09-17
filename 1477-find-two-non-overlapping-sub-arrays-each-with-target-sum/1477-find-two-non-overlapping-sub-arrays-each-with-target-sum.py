class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = 10**9
        left = [INF] * n
        right = [INF] * n
        
        l = 0
        curr_sum = 0
        for r in range(n):
            curr_sum += arr[r]
            while curr_sum > target and l <= r:
                curr_sum -= arr[l]
                l += 1
            if curr_sum == target:
                length = r - l + 1
                left[r] = min(left[r], length)
                right[l] = min(right[l], length)
        
        # prefix min on left
        for i in range(1, n):
            left[i] = min(left[i], left[i-1])
        # suffix min on right
        for i in range(n-2, -1, -1):
            right[i] = min(right[i], right[i+1])
        
        ans = INF
        for i in range(n-1):
            if left[i] != INF and right[i+1] != INF:
                ans = min(ans, left[i] + right[i+1])
        
        return ans if ans != INF else -1