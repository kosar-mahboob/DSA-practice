MOD = 10**9 + 7

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS to find maximum depth from node 1
        dist = [-1] * (n + 1)
        dist[1] = 0
        q = deque([1])
        max_depth = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    if dist[v] > max_depth:
                        max_depth = dist[v]
                    q.append(v)
        
        # Number of edges in the longest root-to-leaf path = max_depth
        # Number of assignments with odd sum = 2^(max_depth - 1)
        if max_depth == 0:
            return 0
        return pow(2, max_depth - 1, MOD)
