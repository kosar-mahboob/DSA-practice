class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.sz = [1] * n
    
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.par[rb] = ra
        self.sz[ra] += self.sz[rb]

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        
        # Since nums is sorted, we can connect adjacent nodes if diff <= maxDiff
        # Because if two nodes are connected, it means they are in the same component
        # Adjacent check is sufficient because if there's a path between non-adjacent nodes,
        # it would go through intermediate nodes, and we'll catch those edges.
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                dsu.union(i, i + 1)
        
        ans = []
        for u, v in queries:
            ans.append(dsu.find(u) == dsu.find(v))
        return ans