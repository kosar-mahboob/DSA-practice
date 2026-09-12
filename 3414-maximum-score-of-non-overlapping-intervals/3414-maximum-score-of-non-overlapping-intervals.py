class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Attach original index
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        arr.sort(key=lambda x: x[1])           # sort by end time
        rs = [x[1] for x in arr]
        pref = [[None] * (n + 1) for _ in range(5)]

        def better(s1, s2):
            if s1 is None: return s2
            if s2 is None: return s1
            if s1[0] > s2[0]: return s1
            if s1[0] < s2[0]: return s2
            return s1 if s1[1] < s2[1] else s2

        for i in range(n):
            l, r, w, idx = arr[i]
            dp_cur = [None] * 5
            dp_cur[1] = (w, (idx,))

            for c in range(2, 5):
                p = bisect_left(rs, l) - 1      # last interval with end < l
                if p >= 0:
                    prev = pref[c - 1][p + 1]
                    if prev is not None:
                        new_w = prev[0] + w
                        new_idx = tuple(sorted(prev[1] + (idx,)))
                        dp_cur[c] = (new_w, new_idx)

            for c in range(1, 5):
                pref[c][i + 1] = better(pref[c][i], dp_cur[c])

        best = None
        for c in range(1, 5):
            best = better(best, pref[c][n])

        return list(best[1]) if best else []