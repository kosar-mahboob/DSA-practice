from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1
        
        # Handle 1 specially
        if freq[1] > 0:
            if freq[1] % 2 == 1:
                ans = max(ans, freq[1])
            else:
                ans = max(ans, freq[1] - 1)
        
        for x in freq:
            if x == 1:
                continue
            cur = x
            pairs = 0
            while freq.get(cur, 0) >= 2:
                pairs += 1
                if cur > 10**9 // cur:
                    break
                cur = cur * cur
            
            # Check if we can use cur as center
            if freq.get(cur, 0) >= 1:
                ans = max(ans, 2 * pairs + 1)
            # If not, use the previous value as center (if we had at least one pair)
            elif pairs > 0:
                # The previous value in the chain exists (has >= 2 copies)
                ans = max(ans, 2 * (pairs - 1) + 1)
        
        return ans