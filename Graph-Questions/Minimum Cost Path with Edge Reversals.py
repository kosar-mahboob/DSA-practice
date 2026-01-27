import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency lists
        adj = [[] for _ in range(n)]
        incoming_edges = [[] for _ in range(n)]
        
        for u, v, w in edges:
            adj[u].append((v, w))
            incoming_edges[u].append((v, w))  # Actually wait, this is for edges v→u
            
        # Wait, incoming_edges[u] should store edges that end at u
        # Let me redo this properly
        incoming = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            incoming[v].append((u, w))  # edge u→v, so for node v, incoming from u
            
        # State graph: 2*n nodes
        # state = u*2 + 0: at u, haven't used u's switch
        # state = u*2 + 1: at u, have used u's switch
        
        dist = [float('inf')] * (2 * n)
        start = 0 * 2 + 0  # (0, 0)
        dist[start] = 0
        heap = [(0, start)]
        
        while heap:
            cost, state = heapq.heappop(heap)
            if cost > dist[state]:
                continue
                
            u = state // 2
            switch_used = state % 2
            
            # If at u and haven't used u's switch
            if switch_used == 0:
                # Option 1: Use u's switch on any incoming edge v→u
                for v, w in incoming[u]:
                    # Reverse v→u to u→v and traverse to v
                    # Arrive at v with v's switch unused (state 0)
                    next_state = v * 2 + 0
                    new_cost = cost + 2 * w
                    if new_cost < dist[next_state]:
                        dist[next_state] = new_cost
                        heapq.heappush(heap, (new_cost, next_state))
                
                # Option 2: Take normal outgoing edges from u
                for v, w in adj[u]:
                    # Go to v with v's switch unused
                    next_state = v * 2 + 0
                    new_cost = cost + w
                    if new_cost < dist[next_state]:
                        dist[next_state] = new_cost
                        heapq.heappush(heap, (new_cost, next_state))
                        
                # Also, we can choose not to use u's switch
                # and transition to (u, 1) state
                next_state = u * 2 + 1
                if cost < dist[next_state]:
                    dist[next_state] = cost
                    heapq.heappush(heap, (cost, next_state))
            
            # If at u and have used u's switch (or chose not to use it)
            if switch_used == 1:
                # Can only take normal outgoing edges
                for v, w in adj[u]:
                    next_state = v * 2 + 0
                    new_cost = cost + w
                    if new_cost < dist[next_state]:
                        dist[next_state] = new_cost
                        heapq.heappush(heap, (new_cost, next_state))
        
        # Check both states for target
        target0 = (n-1) * 2 + 0
        target1 = (n-1) * 2 + 1
        result = min(dist[target0], dist[target1])
        
        return result if result != float('inf') else -1
