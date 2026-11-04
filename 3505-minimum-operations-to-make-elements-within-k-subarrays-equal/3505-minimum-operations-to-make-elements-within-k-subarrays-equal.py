from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        INF = float('inf')

        # Sliding window median with two heaps (lazy deletion)
        lo = []   # max-heap (store negatives)
        hi = []   # min-heap
        lo_del = defaultdict(int)
        hi_del = defaultdict(int)
        lo_sum = 0
        hi_sum = 0
        lo_size = 0
        hi_size = 0

        def prune():
            while lo and lo_del[-lo[0]] > 0:
                lo_del[-lo[0]] -= 1
                heapq.heappop(lo)
            while hi and hi_del[hi[0]] > 0:
                hi_del[hi[0]] -= 1
                heapq.heappop(hi)

        def rebalance():
            nonlocal lo_sum, hi_sum, lo_size, hi_size
            prune()
            while lo_size > hi_size + 1:
                v = -heapq.heappop(lo)
                lo_sum -= v
                lo_size -= 1
                heapq.heappush(hi, v)
                hi_sum += v
                hi_size += 1
                prune()
            while hi_size > lo_size:
                v = heapq.heappop(hi)
                hi_sum -= v
                hi_size -= 1
                heapq.heappush(lo, -v)
                lo_sum += v
                lo_size += 1
                prune()

        def add(v):
            nonlocal lo_sum, hi_sum, lo_size, hi_size
            if lo and v <= -lo[0]:
                heapq.heappush(lo, -v)
                lo_sum += v
                lo_size += 1
            else:
                heapq.heappush(hi, v)
                hi_sum += v
                hi_size += 1
            rebalance()

        def remove(v):
            nonlocal lo_sum, hi_sum, lo_size, hi_size
            if lo and v <= -lo[0]:
                lo_del[v] += 1
                lo_sum -= v
                lo_size -= 1
            else:
                hi_del[v] += 1
                hi_sum -= v
                hi_size -= 1
            rebalance()

        def median_cost():
            # median is top of lo when lo_size >= hi_size
            m = -lo[0]
            return m * lo_size - lo_sum + hi_sum - m * hi_size

        cost = [INF] * n
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                cost[i - x + 1] = median_cost()

        # DP over k windows
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x and cost[i - x] != INF:
                    cand = prev[i - x] + cost[i - x]
                    if cand < cur[i]:
                        cur[i] = cand
            prev = cur

        return prev[n]