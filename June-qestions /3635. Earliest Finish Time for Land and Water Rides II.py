
class Solution:
    def minFinishTime(self,
                      landStartTime: List[int],
                      landDuration: List[int],
                      waterStartTime: List[int],
                      waterDuration: List[int]) -> int:
        # Preprocess water rides for f(x) = min_j (max(ws_j, x) + wd_j)
        water = sorted(zip(waterStartTime, waterDuration))
        m = len(water)
        ws = [w[0] for w in water]
        wd = [w[1] for w in water]
        # prefix min of duration
        pref_min_d = [0] * m
        cur = float('inf')
        for i in range(m):
            cur = min(cur, wd[i])
            pref_min_d[i] = cur
        # suffix min of (ws + wd)
        suff_min_wsd = [0] * m
        cur = float('inf')
        for i in range(m-1, -1, -1):
            cur = min(cur, ws[i] + wd[i])
            suff_min_wsd[i] = cur

        def f(x: int) -> int:
            # number of water rides with start <= x
            idx = bisect.bisect_right(ws, x)  # first index with ws > x
            best = float('inf')
            if idx > 0:
                best = min(best, x + pref_min_d[idx-1])
            if idx < m:
                best = min(best, suff_min_wsd[idx])
            return best

        # Preprocess land rides for g(y) = min_i (max(ls_i, y) + ld_i)
        land = sorted(zip(landStartTime, landDuration))
        n = len(land)
        ls = [l[0] for l in land]
        ld = [l[1] for l in land]
        pref_min_ld = [0] * n
        cur = float('inf')
        for i in range(n):
            cur = min(cur, ld[i])
            pref_min_ld[i] = cur
        suff_min_lsd = [0] * n
        cur = float('inf')
        for i in range(n-1, -1, -1):
            cur = min(cur, ls[i] + ld[i])
            suff_min_lsd[i] = cur

        def g(y: int) -> int:
            idx = bisect.bisect_right(ls, y)
            best = float('inf')
            if idx > 0:
                best = min(best, y + pref_min_ld[idx-1])
            if idx < n:
                best = min(best, suff_min_lsd[idx])
            return best

        # Compute minimal finish time over both orders
        ans = float('inf')
        # Land first: for each land i, use f(landStart[i] + landDuration[i])
        for i in range(len(landStartTime)):
            end = landStartTime[i] + landDuration[i]
            ans = min(ans, f(end))
        # Water first: for each water j, use g(waterStart[j] + waterDuration[j])
        for j in range(len(waterStartTime)):
            end = waterStartTime[j] + waterDuration[j]
            ans = min(ans, g(end))

        return ans
