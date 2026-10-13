class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        n = len(sq)
        pos_count = (n + 1) // 2  # indices 0, 2, 4, ...
        small = sq[:n - pos_count]   # the n - pos_count smallest go to '-' positions
        large = sq[n - pos_count:]   # the rest (pos_count largest) go to '+' positions
        return sum(large) - sum(small)