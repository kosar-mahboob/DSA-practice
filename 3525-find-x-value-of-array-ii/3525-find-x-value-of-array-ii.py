class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        
        n = len(nums)
        size = 4 * n
        tree_total = [0] * size
        tree_cnt = [[0] * k for _ in range(size)]
        
        def build(node, l, r):
            if l == r:
                val = nums[l] % k
                tree_total[node] = val
                tree_cnt[node][val] = 1
                return
            mid = (l + r) // 2
            build(node*2, l, mid)
            build(node*2+1, mid+1, r)
            left, right = node*2, node*2+1
            tree_total[node] = (tree_total[left] * tree_total[right]) % k
            cnt = [0] * k
            for rem in range(k):
                cnt[rem] = tree_cnt[left][rem]
            for rem in range(k):
                if tree_cnt[right][rem]:
                    cnt[(tree_total[left] * rem) % k] += tree_cnt[right][rem]
            tree_cnt[node] = cnt
        
        def update(node, l, r, idx, val):
            if l == r:
                v = val % k
                tree_total[node] = v
                for i in range(k):
                    tree_cnt[node][i] = 0
                tree_cnt[node][v] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(node*2, l, mid, idx, val)
            else:
                update(node*2+1, mid+1, r, idx, val)
            left, right = node*2, node*2+1
            tree_total[node] = (tree_total[left] * tree_total[right]) % k
            cnt = [0] * k
            for rem in range(k):
                cnt[rem] = tree_cnt[left][rem]
            for rem in range(k):
                if tree_cnt[right][rem]:
                    cnt[(tree_total[left] * rem) % k] += tree_cnt[right][rem]
            tree_cnt[node] = cnt
        
        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree_total[node], tree_cnt[node][:]
            mid = (l + r) // 2
            if qr <= mid:
                return query(node*2, l, mid, ql, qr)
            if ql > mid:
                return query(node*2+1, mid+1, r, ql, qr)
            lt, lc = query(node*2, l, mid, ql, qr)
            rt, rc = query(node*2+1, mid+1, r, ql, qr)
            total = (lt * rt) % k
            cnt = [0] * k
            for rem in range(k):
                cnt[rem] = lc[rem]
            for rem in range(k):
                if rc[rem]:
                    cnt[(lt * rem) % k] += rc[rem]
            return total, cnt
        
        build(1, 0, n-1)
        res = []
        for idx, val, start, x in queries:
            update(1, 0, n-1, idx, val)
            if start >= n:
                res.append(0)
                continue
            _, cnt = query(1, 0, n-1, start, n-1)
            res.append(cnt[x] if x < k else 0)
        return res