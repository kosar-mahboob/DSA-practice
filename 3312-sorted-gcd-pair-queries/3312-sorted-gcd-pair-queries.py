from typing import List
from collections import Counter
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Count frequency of each number
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
        
        # Count how many numbers are divisible by each d
        count_div = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            total = 0
            for multiple in range(d, max_val + 1, d):
                total += freq[multiple]
            count_div[d] = total * (total - 1) // 2
        
        # Count pairs with GCD exactly equal to d using inclusion-exclusion
        exact_gcd = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            total_pairs = count_div[d]
            for multiple in range(2 * d, max_val + 1, d):
                total_pairs -= exact_gcd[multiple]
            exact_gcd[d] = total_pairs
        
        # Build prefix sum over GCD values
        prefix = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + exact_gcd[i]
        
        # Answer queries using binary search
        ans = []
        for q in queries:
            lo, hi = 1, max_val
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            ans.append(lo)
        
        return ans