class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        size = 1
        while size < n:
            size <<= 1

        N = 2 * size
        L = [0] * N
        lc = [-1] * N
        rc = [-1] * N
        ll = [0] * N
        rl = [0] * N
        mx = [0] * N

        # Build leaves
        for i in range(size):
            idx = size + i
            if i < n:
                c = ord(s[i]) - 97
                L[idx] = 1
                lc[idx] = rc[idx] = c
                ll[idx] = rl[idx] = mx[idx] = 1

        def pull(i: int):
            a = i << 1
            b = a | 1

            if L[a] == 0:
                L[i] = L[b]
                lc[i] = lc[b]
                rc[i] = rc[b]
                ll[i] = ll[b]
                rl[i] = rl[b]
                mx[i] = mx[b]
            elif L[b] == 0:
                L[i] = L[a]
                lc[i] = lc[a]
                rc[i] = rc[a]
                ll[i] = ll[a]
                rl[i] = rl[a]
                mx[i] = mx[a]
            else:
                L[i] = L[a] + L[b]
                lc[i] = lc[a]
                rc[i] = rc[b]

                ll[i] = ll[a]
                if ll[a] == L[a] and rc[a] == lc[b]:
                    ll[i] = L[a] + ll[b]

                rl[i] = rl[b]
                if rl[b] == L[b] and lc[b] == rc[a]:
                    rl[i] = L[b] + rl[a]

                mx[i] = max(mx[a], mx[b])
                if rc[a] == lc[b]:
                    cross = rl[a] + ll[b]
                    if cross > mx[i]:
                        mx[i] = cross

        # Build segment tree
        for i in range(size - 1, 0, -1):
            pull(i)

        ans = []
        for pos, ch in zip(queryIndices, queryCharacters):
            c = ord(ch) - 97
            idx = size + pos

            L[idx] = 1
            lc[idx] = rc[idx] = c
            ll[idx] = rl[idx] = mx[idx] = 1

            idx >>= 1
            while idx:
                pull(idx)
                idx >>= 1

            ans.append(mx[1])

        return ans