from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        # Group indices by their value
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)

        min_span = float('inf')
        for indices in pos.values():
            m = len(indices)
            if m >= 3:
                # Check every consecutive triple to find minimal span
                for i in range(m - 2):
                    span = indices[i+2] - indices[i]
                    if span < min_span:
                        min_span = span

        return 2 * min_span if min_span != float('inf') else -1
