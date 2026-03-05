class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        # Count mismatches when starting with '0' at even indices
        mismatches = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                mismatches += 1
        # For the other pattern, mismatches = n - mismatches
        return min(mismatches, n - mismatches)
