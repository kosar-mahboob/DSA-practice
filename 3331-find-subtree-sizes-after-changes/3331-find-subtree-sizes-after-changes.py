class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}
        stack = [(0, 0, None)]

        while stack:
            node, phase, old = stack.pop()
            if phase == 0:
                c = s[node]
                if c in last and node != 0:
                    new_parent[node] = last[c]
                prev = last.get(c)
                last[c] = node
                stack.append((node, 1, prev))
                for ch in children[node]:
                    stack.append((ch, 0, None))
            else:
                c = s[node]
                if old is None:
                    last.pop(c, None)
                else:
                    last[c] = old

        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        size = [1] * n
        order = []
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            for ch in new_children[node]:
                stack.append(ch)

        for node in reversed(order):
            for ch in new_children[node]:
                size[node] += size[ch]

        return size