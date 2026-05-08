from typing import List

class Solution:
    def maxReachableValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        stack = []                     # (max_val, list_of_indices)
        
        for i, v in enumerate(nums):
            cur_max = v
            cur_indices = [i]
            # merge with all components that have any element > v
            while stack and stack[-1][0] > v:
                prev_max, prev_indices = stack.pop()
                cur_max = max(cur_max, prev_max)
                cur_indices.extend(prev_indices)
            stack.append((cur_max, cur_indices))
            
        for max_val, indices in stack:
            for idx in indices:
                ans[idx] = max_val
        return ans
