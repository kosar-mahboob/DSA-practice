from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid
        arr = [val for row in grid for val in row]
        
        # Check remainder modulo x
        rem = arr[0] % x
        for val in arr:
            if val % x != rem:
                return -1
        
        # Sort and find median
        arr.sort()
        median = arr[len(arr) // 2]
        
        # Compute total operations
        ops = 0
        for val in arr:
            ops += abs(val - median) // x
        return ops
