from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        # Step 1: rotate 90 degrees clockwise
        res = [['.'] * m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                ch = boxGrid[r][c]
                new_r, new_c = c, m - 1 - r
                res[new_r][new_c] = ch
        
        # Step 2: apply gravity in each column (downwards)
        for col in range(m):  # number of columns in res = m
            write = n - 1  # bottom row index
            for row in range(n - 1, -1, -1):
                if res[row][col] == '*':
                    write = row - 1
                elif res[row][col] == '#':
                    if write != row:
                        res[write][col] = '#'
                        res[row][col] = '.'
                    write -= 1
        return res
