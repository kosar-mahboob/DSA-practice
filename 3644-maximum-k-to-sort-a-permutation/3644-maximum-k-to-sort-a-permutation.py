class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        # find positions where nums[i] != i — these are the elements that need to move
        mis = [nums[i] for i in range(n) if nums[i] != i]
        if not mis:
            return 0
        ans = mis[0]
        for v in mis[1:]:
            ans &= v
        return ans