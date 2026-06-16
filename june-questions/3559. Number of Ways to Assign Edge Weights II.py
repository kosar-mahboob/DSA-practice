from typing import List
from collections import deque

MOD = 10**9 + 7
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS to compute depth and parent (binary lifting)
        LOG = (n).bit_length()
        parent = [[-1] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        
        q = deque([1])
        depth[1] = 0
        parent[0][1] = -1
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v != parent[0][u]:
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        
        for k in range(1, LOG):
            for v in range(1, n + 1):
                if parent[k-1][v] != -1:
                    parent[k][v] = parent[k-1][parent[k-1][v]]
                else:
                    parent[k][v] = -1
        
        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            for k in range(LOG-1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]
        
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            l = lca(u, v)
            L = depth[u] + depth[v] - 2 * depth[l]
            ans.append(pow(2, L-1, MOD))
        return ans
