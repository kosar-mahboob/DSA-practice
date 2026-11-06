class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        all_times = sorted((t, sid) for sid, t in logs)
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        res = [0] * len(queries)
        active = {}
        L = R = 0
        m = len(all_times)

        for qi in order:
            q = queries[qi]
            while R < m and all_times[R][0] <= q:
                sid = all_times[R][1]
                active[sid] = active.get(sid, 0) + 1
                R += 1
            while L < m and all_times[L][0] < q - x:
                sid = all_times[L][1]
                active[sid] -= 1
                if active[sid] == 0:
                    del active[sid]
                L += 1
            res[qi] = n - len(active)

        return res