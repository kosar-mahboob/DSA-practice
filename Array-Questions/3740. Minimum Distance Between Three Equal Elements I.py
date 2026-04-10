from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Group indices by their value
        positions = defaultdict(list)
        for i, val in enumerate(nums):
            positions[val].append(i)
        
        ans = float('inf')
        for indices in positions.values():
            if len(indices) >= 3:
                # Check consecutive triples to minimize span (max - min)
                for i in range(len(indices) - 2):
                    span = indices[i+2] - indices[i]
                    ans = min(ans, 2 * span)
        
        return ans if ans != float('inf') else -1
