from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        # F(0) = sum(i * nums[i])
        cur = sum(i * v for i, v in enumerate(nums))
        ans = cur
        for k in range(1, n):
            # F(k) = F(k-1) + total - n * nums[n - k]
            cur = cur + total - n * nums[n - k]
            ans = max(ans, cur)
        return ans
