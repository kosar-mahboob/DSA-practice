class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Sort values together with their original indices
        pairs = sorted((v, i) for i, v in enumerate(nums))

        ans = [0] * n
        i = 0
        while i < n:
            vals = []
            idxs = []
            j = i
            # Group elements that can be swapped transitively
            while j < n:
                if j > i and pairs[j][0] - pairs[j - 1][0] > limit:
                    break
                vals.append(pairs[j][0])
                idxs.append(pairs[j][1])
                j += 1

            # Place sorted values at sorted indices to get lexicographically smallest
            idxs.sort()
            for pos, val in zip(idxs, vals):
                ans[pos] = val

            i = j

        return ans