class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        
        # Build prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        
        # Helper to get sum of square with top-left (r, c) and side length k
        def square_sum(r, c, k):
            # r, c are 0-indexed
            r2, c2 = r + k - 1, c + k - 1
            return (
                prefix[r2 + 1][c2 + 1] - 
                prefix[r][c2 + 1] - 
                prefix[r2 + 1][c] + 
                prefix[r][c]
            )
        
        # Binary search on side length
        low, high = 0, min(m, n)
        best = 0
        
        while low <= high:
            mid = (low + high) // 2
            found = False
            
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if square_sum(i, j, mid) <= threshold:
                        found = True
                        break
                if found:
                    break
            
            if found:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return best
