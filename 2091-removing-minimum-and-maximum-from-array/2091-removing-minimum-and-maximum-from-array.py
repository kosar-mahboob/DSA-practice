class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        min_idx = max_idx = 0
        for i in range(1, n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i

        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)

        return min(b + 1, n - a, a + 1 + n - b)