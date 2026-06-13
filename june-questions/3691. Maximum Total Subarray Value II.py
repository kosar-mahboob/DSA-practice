class SparseTable:
    def __init__(self, arr, func):
        self.n = len(arr)
        self.func = func
        k = self.n.bit_length()
        self.st = [arr[:]]
        j = 1
        while (1 << j) <= self.n:
            prev = self.st[-1]
            step = 1 << (j - 1)
            cur = [func(prev[i], prev[i + step]) for i in range(self.n - (1 << j) + 1)]
            self.st.append(cur)
            j += 1

    def query(self, l, r):
        length = r - l + 1
        j = length.bit_length() - 1
        return self.func(self.st[j][l], self.st[j][r - (1 << j) + 1])


class Solution:
    def maxTotalSubarrayValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Build sparse tables for range max and min
        max_table = SparseTable(nums, max)
        min_table = SparseTable(nums, min)

        def value(l, r):
            return max_table.query(l, r) - min_table.query(l, r)

        # Max-heap using negative values
        heap = []
        # For each starting index l, start with the largest r = n-1
        for l in range(n):
            r = n - 1
            heapq.heappush(heap, (-value(l, r), l, r))

        total = 0
        for _ in range(k):
            neg_val, l, r = heapq.heappop(heap)
            total += -neg_val
            # Push next best for the same l: r-1 if valid
            if r - 1 >= l:
                heapq.heappush(heap, (-value(l, r - 1), l, r - 1))

        return total
