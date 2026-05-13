from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # difference array for sums in [2, 2*limit]
        diff = [0] * (2 * limit + 2)   # index up to 2*limit + 1
        
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            if a > b:
                a, b = b, a
            
            # cost 2 everywhere by default
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            
            # cost 1 for [a+1, limit+b]
            diff[a + 1] -= 1
            diff[limit + b + 1] += 1
            
            # cost 0 for exactly a+b
            diff[a + b] -= 1
            diff[a + b + 1] += 1
        
        ans = n  # maximum possible moves
        cur = 0
        for s in range(2, 2 * limit + 1):
            cur += diff[s]
            if cur < ans:
                ans = cur
        return ans
