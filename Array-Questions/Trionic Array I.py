#leetcode problem no : 3637 Trionic Array I
from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for p in range(1, n-2):          # 0 < p < n-2 at most, because q < n-1 and q > p
            for q in range(p+1, n-1):    # p < q < n-1
                # Check nums[0..p] strictly increasing
                inc1 = all(nums[i] < nums[i+1] for i in range(p))
                # Check nums[p..q] strictly decreasing
                dec = all(nums[i] > nums[i+1] for i in range(p, q))
                # Check nums[q..n-1] strictly increasing
                inc2 = all(nums[i] < nums[i+1] for i in range(q, n-1))
                
                if inc1 and dec and inc2:
                    return True
        return False
