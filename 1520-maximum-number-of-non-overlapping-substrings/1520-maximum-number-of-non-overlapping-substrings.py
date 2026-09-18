class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        from typing import List
from functools import lru_cache

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = [-1] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        intervals_set = set()
        for c in range(26):
            if first[c] != -1:
                L, R = first[c], last[c]
                while True:
                    newL, newR = L, R
                    for i in range(L, R + 1):
                        idx = ord(s[i]) - ord('a')
                        if first[idx] < newL:
                            newL = first[idx]
                        if last[idx] > newR:
                            newR = last[idx]
                    if newL == L and newR == R:
                        break
                    L, R = newL, newR
                intervals_set.add((L, R))

        intervals = sorted(intervals_set, key=lambda x: x[0])
        m = len(intervals)
        next_idx = [m] * m
        for i in range(m):
            L, R = intervals[i]
            j = i + 1
            while j < m and intervals[j][0] <= R:
                j += 1
            next_idx[i] = j

        @lru_cache(None)
        def dp(i):
            if i == m:
                return (0, 0, ())
            skip = dp(i + 1)
            L, R = intervals[i]
            length = R - L + 1
            take = dp(next_idx[i])
            take_count = take[0] + 1
            take_len = take[1] + length
            take_tuple = (s[L:R+1],) + take[2]
            if take_count > skip[0] or (take_count == skip[0] and take_len < skip[1]):
                return (take_count, take_len, take_tuple)
            return skip

        return list(dp(0)[2])