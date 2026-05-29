from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        min_val = float('inf')
        for num in nums:
            val = digit_sum(num)
            if val < min_val:
                min_val = val
        return min_val
