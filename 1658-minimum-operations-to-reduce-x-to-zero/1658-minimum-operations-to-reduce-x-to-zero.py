class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        left = 0
        curr = 0
        max_len = -1
        for right in range(len(nums)):
            curr += nums[right]
            while curr > target and left <= right:
                curr -= nums[left]
                left += 1
            if curr == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != -1 else -1