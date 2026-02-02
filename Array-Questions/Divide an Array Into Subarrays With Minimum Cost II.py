#leetcode problem no : 3013  Divide an Array Into Subarrays With Minimum Cost II
from sortedcontainers import SortedList
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        res = nums[0]
        need = k - 1  # Number of additional elements needed
        
        # Use two SortedLists for efficient sliding window k-smallest
        left = SortedList()  # Will contain at most 'need' smallest elements
        right = SortedList()  # Contains the rest
        left_sum = 0
        
        best = float('inf')
        
        # We'll slide the window starting at each position
        for i in range(1, n):
            # Remove element that's dist+1 behind if it exists
            remove_idx = i - dist - 1
            if remove_idx >= 1:
                val = nums[remove_idx]
                if val in left:
                    left.remove(val)
                    left_sum -= val
                    # Move smallest from right to left if left has less than need elements
                    if right and len(left) < need:
                        move_val = right[0]
                        right.remove(move_val)
                        left.add(move_val)
                        left_sum += move_val
                elif val in right:
                    right.remove(val)
            
            # Add current element
            val = nums[i]
            if len(left) < need:
                left.add(val)
                left_sum += val
            elif val < left[-1]:
                # Move largest from left to right
                move_val = left[-1]
                left.remove(move_val)
                left_sum -= move_val
                right.add(move_val)
                
                # Add new element to left
                left.add(val)
                left_sum += val
            else:
                right.add(val)
            
            # Check if we have a valid window starting at some position
            if i >= dist + 1:
                # The window [i-dist, i] is complete
                # The starting position of this window would be i-dist
                start_pos = i - dist
                if len(left) == need:
                    # We have 'need' smallest elements in window
                    best = min(best, left_sum)
        
        return res + best
