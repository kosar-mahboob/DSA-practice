class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
    
        n = len(online)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        
        # Binary search on answer
        # Check if there exists a valid path with minimum edge cost >= mid
        def can(mid: int) -> bool:
            # Only consider edges with cost >= mid
            # Need to find path from 0 to n-1 with total cost <= k
            
            # Topological order (DAG)
            indegree = [0] * n
            for u in range(n):
                for v, w in adj[u]:
                    if w >= mid:
                        indegree[v] += 1
            
            # DP: shortest distance to each node using only edges with cost >= mid
            dist = [float('inf')] * n
            dist[0] = 0
            
            q = deque()
            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)
            
            topo = []
            while q:
                u = q.popleft()
                topo.append(u)
                for v, w in adj[u]:
                    if w >= mid:
                        indegree[v] -= 1
                        if indegree[v] == 0:
                            q.append(v)
            
            # If n-1 not in topo, no path using valid edges
            # Actually need to check reachability with DP
            # Do DP in topological order
            dist = [float('inf')] * n
            dist[0] = 0
            
            # Process nodes in topological order
            for u in topo:
                if dist[u] == float('inf') or not online[u]:
                    continue
                for v, w in adj[u]:
                    if w >= mid and online[v]:
                        if dist[v] > dist[u] + w:
                            dist[v] = dist[u] + w
            
            return dist[n-1] <= k
        
        # Collect all possible edge costs
        costs = sorted(set(w for _, _, w in edges))
        if not costs:
            return -1
        
        # Binary search on costs
        lo, hi = 0, len(costs) - 1
        ans = -1
        while lo <= hi:
            mid_idx = (lo + hi) // 2
            if can(costs[mid_idx]):
                ans = costs[mid_idx]
                lo = mid_idx + 1
            else:
                hi = mid_idx - 1
        
        return ans