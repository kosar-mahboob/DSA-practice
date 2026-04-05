class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # For each row, find the column of the rightmost 1 (or -1 if none)
        req = []
        
        for row in grid:
            # scan from right to left
            rightmost = -1
            
            for j in range(n-1, -1, -1):
                if row[j] == 1:
                    rightmost = j
                    break
            req.append(rightmost)   
            # -1 means no ones
        
        # Current list of requirements in original order
        cur = req[:]
        swaps = 0
        for i in range(n):
            # Find the first row from position i onward that can be placed at row i
            found = -1
            for j in range(i, n):
                if cur[j] <= i:
                    found = j
                    break
            if found == -1:
                return -1
            # Bring that row up to position i
            swaps += found - i
            # Remove it from found and insert at i
            row_to_move = cur.pop(found)
            cur.insert(i, row_to_move)
        return swaps
