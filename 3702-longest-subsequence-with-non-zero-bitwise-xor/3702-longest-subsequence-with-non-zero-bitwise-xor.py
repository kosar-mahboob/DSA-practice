class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        for x in nums:
            total_xor ^= x

        if total_xor != 0:
            return len(nums)

        # total_xor == 0
        # If all elements are zero, no non-zero XOR subsequence exists
        if all(x == 0 for x in nums):
            return 0

        # Remove any non-zero element → XOR becomes that element ≠ 0
        return len(nums) - 1