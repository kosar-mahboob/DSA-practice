from typing import List
from math import isqrt

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # divisors of each length (excluding the length itself and 1? No — d can be any proper divisor)
        divs = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for m in range(2 * d, n + 1, d):
                divs[m].append(d)

        # cost[l][r] = min changes to make s[l..r] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]

        for l in range(n):
            for r in range(l + 1, n):
                L = r - l + 1
                if L < 2:
                    continue
                best = INF
                for d in divs[L]:
                    total = 0
                    for start in range(l, l + d):
                        # collect the group: positions start, start+d, start+2d, ...
                        group = []
                        p = start
                        while p <= r:
                            group.append(s[p])
                            p += d
                        # count changes to make this group a palindrome
                        i, j = 0, len(group) - 1
                        while i < j:
                            if group[i] != group[j]:
                                total += 1
                            i += 1
                            j -= 1
                    if total < best:
                        best = total
                cost[l][r] = best

        # dp[i][j] = min changes to split s[0..i-1] into j semi-palindromes
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                for p in range(j - 1, i):
                    if dp[p][j - 1] == INF or cost[p][i - 1] == INF:
                        continue
                    if p == i:
                        continue
                    cand = dp[p][j - 1] + cost[p][i - 1]
                    if cand < dp[i][j]:
                        dp[i][j] = cand
        return dp[n][k]