class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        from typing import List
from bisect import bisect_left

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pref = [0] * (n + 1)
        for i, v in enumerate(stoneValue):
            pref[i + 1] = pref[i] + v

        dp = [[0] * n for _ in range(n)]

        # Left case helpers for each start index l
        ptr = list(range(n))
        maxLeft = [-10**18] * n

        for r in range(n):
            # suffix max for right case:
            # suf[t] = max(dp[t][r] - pref[t]) over t..r
            suf = [-10**18] * (n + 2)
            suf[r] = dp[r][r] - pref[r]   # dp[r][r] == 0

            for l in range(r - 1, -1, -1):
                target = pref[l] + pref[r + 1]
                best = 0

                # Left sum < right sum
                mid = ptr[l]
                while mid < r and 2 * pref[mid + 1] < target:
                    cand = dp[l][mid] + pref[mid + 1]
                    if cand > maxLeft[l]:
                        maxLeft[l] = cand
                    mid += 1
                ptr[l] = mid
                if maxLeft[l] != -10**18:
                    best = max(best, maxLeft[l] - pref[l])

                # Left sum > right sum
                q = bisect_left(pref, target // 2 + 1, l + 1, r + 1)
                if q <= r:
                    best = max(best, suf[q] + pref[r + 1])

                # Left sum == right sum
                if target % 2 == 0:
                    half = target // 2
                    idx = bisect_left(pref, half, l + 1, r + 1)
                    if idx <= r and pref[idx] == half:
                        left_sum = pref[idx] - pref[l]
                        eq = left_sum + max(dp[l][idx - 1], dp[idx][r])
                        best = max(best, eq)

                dp[l][r] = best

                # Update suffix max for upcoming smaller l values
                val = dp[l][r] - pref[l]
                suf[l] = val if val > suf[l + 1] else suf[l + 1]

        return dp[0][n - 1]