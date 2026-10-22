from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        target = list(range(n))
        if nums == target:
            return 0
        
        def rot_dist(arr, goal):
            try:
                p = arr.index(goal[0])
            except ValueError:
                return float('inf')
            if arr[p:] + arr[:p] == goal:
                return p
            return float('inf')
        
        ans = float('inf')
        r = rot_dist(nums, target)
        d = rot_dist(nums[::-1], target)
        e = rot_dist(nums, target[::-1])
        
        if r != float('inf'):
            ans = min(ans, r, n - r + 2)
        if d != float('inf'):
            ans = min(ans, 1 + d)
        if e != float('inf'):
            ans = min(ans, 1 + e)
        
        return ans if ans != float('inf') else -1