from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Store all prefixes of numbers in arr1
        prefixes = set()
        for num in arr1:
            # Generate all prefixes of num (including num itself)
            while num > 0:
                prefixes.add(num)
                num //= 10
        
        max_len = 0
        for num in arr2:
            # Check prefixes of num from longest to shortest
            while num > 0:
                if num in prefixes:
                    # Compute the number of digits
                    length = len(str(num))
                    if length > max_len:
                        max_len = length
                    # No need to check shorter prefixes for this num
                    break
                num //= 10
        
        return max_len
