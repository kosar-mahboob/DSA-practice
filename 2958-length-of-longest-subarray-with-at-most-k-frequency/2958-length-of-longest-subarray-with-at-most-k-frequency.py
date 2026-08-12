class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        left = 0
        ans = 0

        for right, x in enumerate(nums):
            freq[x] += 1

            # Shrink window while any element appears more than k times
            while freq[x] > k:
                freq[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans