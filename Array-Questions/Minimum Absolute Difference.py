#leetcode [problem no : 1200. Minimum Absolute Difference
class Solution:
    def minimumAbsDifference(self, arr):
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Find the minimum absolute difference
        min_diff = float('inf')
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            min_diff = min(min_diff, diff)
        
        # Step 3: Collect all pairs with difference equal to min_diff
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1], arr[i]])
        
        return result
