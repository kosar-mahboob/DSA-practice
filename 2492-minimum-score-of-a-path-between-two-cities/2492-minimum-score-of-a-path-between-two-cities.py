class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # BFS/DFS to find all reachable nodes from city 1
        visited = [False] * (n + 1)
        visited[1] = True
        q = deque([1])
        
        while q:
            u = q.popleft()
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # Find minimum edge weight among all edges connected to visited nodes
        ans = float('inf')
        for u in range(1, n + 1):
            if visited[u]:
                for v, w in adj[u]:
                    if visited[v]:
                        ans = min(ans, w)
        
        return ans