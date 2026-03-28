from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        # ----- basic consistency checks -----
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if lcp[i][j] > n - max(i, j):
                    return ""

        for i in range(n):
            for j in range(n):
                if i + 1 < n and j + 1 < n and lcp[i][j] > 0:
                    if lcp[i + 1][j + 1] != lcp[i][j] - 1:
                        return ""

        # ----- DSU for equal positions -----
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx

        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    union(i, j)

        # ----- lcp=0 forces different groups -----
        for i in range(n):
            for j in range(n):
                if lcp[i][j] == 0 and find(i) == find(j):
                    return ""

        # ----- map each root to a group index -----
        root_to_idx = {}
        group_id = [0] * n
        groups = []          # groups[k] = list of indices in group k
        for i in range(n):
            r = find(i)
            if r not in root_to_idx:
                root_to_idx[r] = len(groups)
                groups.append([])
            idx = root_to_idx[r]
            group_id[i] = idx
            groups[idx].append(i)

        g = len(groups)
        # smallest index in each group (for ordering)
        min_idx = [min(group) for group in groups]
        order = sorted(range(g), key=lambda x: min_idx[x])

        # ----- build adjacency (lcp=0) between groups -----
        adj = [set() for _ in range(g)]
        for i in range(n):
            for j in range(n):
                if lcp[i][j] == 0:
                    gi, gj = group_id[i], group_id[j]
                    if gi != gj:
                        adj[gi].add(gj)
                        adj[gj].add(gi)

        # ----- greedy colouring (letters 'a'..'z') -----
        colour = [-1] * g
        for grp in order:
            used = set()
            for nb in adj[grp]:
                if colour[nb] != -1:
                    used.add(colour[nb])
            c = 0
            while c in used:
                c += 1
            if c >= 26:
                return ""
            colour[grp] = c

        # ----- build the candidate string -----
        ans = [''] * n
        for i in range(n):
            ans[i] = chr(ord('a') + colour[group_id[i]])

        # ----- verify that the constructed string matches the given lcp -----
        # compute lcp of ans in O(n^2)
        computed = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if ans[i] == ans[j]:
                    if i + 1 < n and j + 1 < n:
                        computed[i][j] = 1 + computed[i + 1][j + 1]
                    else:
                        computed[i][j] = 1
                else:
                    computed[i][j] = 0

        for i in range(n):
            for j in range(n):
                if computed[i][j] != lcp[i][j]:
                    return ""

        return ''.join(ans)
