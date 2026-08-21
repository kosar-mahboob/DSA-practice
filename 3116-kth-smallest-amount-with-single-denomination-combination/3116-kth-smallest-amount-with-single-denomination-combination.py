class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        size = 1 << n

        # Precompute LCM for every subset of coins
        lcms = [1] * size
        for i, c in enumerate(coins):
            step = 1 << i
            for mask in range(step):
                l = lcms[mask]
                lcms[mask | step] = l // gcd(l, c) * c

        # Inclusion-exclusion sign for each non-empty subset
        signs = [0] * size
        for mask in range(1, size):
            signs[mask] = 1 if mask.bit_count() & 1 else -1

        def count(x: int) -> int:
            """Count distinct multiples of any coin that are <= x."""
            total = 0
            for mask in range(1, size):
                L = lcms[mask]
                if L <= x:
                    total += signs[mask] * (x // L)
            return total

        lo, hi = 0, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo