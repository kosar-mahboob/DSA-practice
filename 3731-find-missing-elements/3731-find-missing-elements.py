class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn, mx = min(nums), max(nums)
        present = set(nums)
        return [x for x in range(mn + 1, mx) if x not in present]