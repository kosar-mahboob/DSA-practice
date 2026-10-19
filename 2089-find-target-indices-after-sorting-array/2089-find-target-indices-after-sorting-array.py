class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = sum(1 for x in nums if x < target)
        count = sum(1 for x in nums if x == target)
        return list(range(less, less + count))