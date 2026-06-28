class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        # First element must be 1
        arr[0] = 1
        # For each next element, cap it to at most previous + 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i-1] + 1)
        return arr[-1]