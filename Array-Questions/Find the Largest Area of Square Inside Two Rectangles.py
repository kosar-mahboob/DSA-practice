from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        
        # Check all pairs of rectangles
        for i in range(n):
            a1, b1 = bottomLeft[i]
            c1, d1 = topRight[i]
            
            for j in range(i + 1, n):
                a2, b2 = bottomLeft[j]
                c2, d2 = topRight[j]
                
                # Find intersection rectangle
                x_left = max(a1, a2)
                x_right = min(c1, c2)
                y_bottom = max(b1, b2)
                y_top = min(d1, d2)
                
                # Check if they intersect
                if x_left < x_right and y_bottom < y_top:
                    width = x_right - x_left
                    height = y_top - y_bottom
                    side = min(width, height)
                    max_side = max(max_side, side)
        
        # Return area = side²
        return max_side * max_side
