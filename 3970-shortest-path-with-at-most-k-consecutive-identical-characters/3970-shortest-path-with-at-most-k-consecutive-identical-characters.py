class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')
        # dist[node][run] = min cost to reach node with current run length = run
        dist = [[INF] * (k + 1) for _ in range(n)]
        start_run = 1
        dist[0][start_run] = 0
        pq = [(0, 0, start_run)]  # (cost, node, run)

        while pq:
            cost, u, run = heapq.heappop(pq)
            if cost > dist[u][run]:
                continue
            if u == n - 1:
                return cost
            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    new_run = run + 1
                    if new_run > k:
                        continue
                else:
                    new_run = 1
                nc = cost + w
                if nc < dist[v][new_run]:
                    dist[v][new_run] = nc
                    heapq.heappush(pq, (nc, v, new_run))

        return -1