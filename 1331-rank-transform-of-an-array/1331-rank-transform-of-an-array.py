class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Get sorted unique values
        sorted_unique = sorted(set(arr))
        # Map each value to its rank (1-indexed)
        rank_map = {val: idx + 1 for idx, val in enumerate(sorted_unique)}
        # Replace each element with its rank
        return [rank_map[val] for val in arr]