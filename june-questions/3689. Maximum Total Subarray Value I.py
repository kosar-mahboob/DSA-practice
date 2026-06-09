from typing import List

class Solution:
    def maxTotalSubarrayValue(self, nums: List[int], k: int) -> int:
        # The maximum possible value of any subarray is max(nums) - min(nums)
        # We can take that same subarray k times to get total = k * (max - min)
        return k * (max(nums) - min(nums))
