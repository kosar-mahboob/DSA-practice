class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        complete_count = 0
        
        for i in range(n):
            if not visited[i]:
                # BFS to find all nodes in this component
                queue = [i]
                visited[i] = True
                component = []
                
                while queue:
                    node = queue.pop()
                    component.append(node)
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # Check if component is complete
                size = len(component)
                # For a complete component of size k, each node should have degree k-1
                # Or total edges should be k * (k-1) // 2
                expected_edges = size * (size - 1) // 2
                actual_edges = 0
                
                for node in component:
                    actual_edges += len(adj[node])
                
                actual_edges //= 2  # Each edge counted twice
                
                if actual_edges == expected_edges:
                    complete_count += 1
        
        return complete_count