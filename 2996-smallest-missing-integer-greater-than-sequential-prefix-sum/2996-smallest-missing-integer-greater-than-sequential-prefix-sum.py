class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        # Find longest sequential prefix
        i = 0
        while i + 1 < n and nums[i + 1] == nums[i] + 1:
            i += 1
        prefix_sum = sum(nums[:i + 1])

        # Find smallest missing integer >= prefix_sum
        s = set(nums)
        x = prefix_sum
        while x in s:
            x += 1
        return x