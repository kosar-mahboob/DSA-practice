class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for u, v in invocations:
            g[u].append(v)
            rg[v].append(u)

        suspicious = set()
        stack = [k]
        while stack:
            u = stack.pop()
            if u not in suspicious:
                suspicious.add(u)
                for v in g[u]:
                    if v not in suspicious:
                        stack.append(v)

        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
        return [i for i in range(n) if i not in suspicious]