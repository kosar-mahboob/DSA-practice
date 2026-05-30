from typing import List

class BIT:
    # Fenwick tree for prefix sums and find_kth
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def sum(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    # smallest index such that prefix sum >= k (1‑based)
    def find_kth(self, k: int) -> int:
        idx = 0
        bit_mask = 1 << (self.n.bit_length())
        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit_mask >>= 1
        return idx + 1


class SegTree:
    # segment tree for range maximum, point updates
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (4 * n)

    def _update(self, node: int, l: int, r: int, idx: int, val: int) -> None:
        if l == r:
            self.tree[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self._update(node * 2, l, mid, idx, val)
        else:
            self._update(node * 2 + 1, mid + 1, r, idx, val)
        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def update(self, idx: int, val: int) -> None:
        self._update(1, 1, self.n, idx, val)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return max(self._query(node * 2, l, mid, ql, qr),
                   self._query(node * 2 + 1, mid + 1, r, ql, qr))

    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 1, self.n, ql, qr)


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # maximum coordinate that can appear (x up to 50000)
        MAX_X = 50000
        bit = BIT(MAX_X)
        seg = SegTree(MAX_X)
        results = []

        for q in queries:
            if q[0] == 1:           # type 1: add obstacle
                x = q[1]
                # find predecessor (largest obstacle < x)
                cnt = bit.sum(x - 1)
                pre = bit.find_kth(cnt) if cnt > 0 else 0
                # find successor (smallest obstacle > x)
                total = bit.sum(MAX_X)
                left = bit.sum(x)
                nxt = None
                if total > left:
                    nxt = bit.find_kth(left + 1)

                # remove the gap (pre, nxt) if it exists
                if nxt is not None:
                    seg.update(nxt, 0)

                # add new gap (pre, x)
                seg.update(x, x - pre)

                # add new gap (x, nxt) if nxt exists
                if nxt is not None:
                    seg.update(nxt, nxt - x)

                # finally mark the obstacle in BIT
                bit.add(x, 1)

            else:                   # type 2: query
                _, x, sz = q
                # predecessor of x (largest obstacle <= x)
                cnt = bit.sum(x)
                last = bit.find_kth(cnt) if cnt > 0 else 0
                candidate = x - last
                # max gap completely inside [0, x]
                best = seg.query(1, x)
                results.append(max(best, candidate) >= sz)

        return results
