class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # Two cases:
        # 1. Product of three largest numbers
        # 2. Product of two smallest (most negative) and largest
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        