# leetcode problem no : 799. Champagne Tower
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # current row: start with the top glass
        current = [float(poured)]
        
        # simulate row by row until we reach the query row
        for r in range(query_row):
            # next row has one more glass than current row
            next_row = [0.0] * (r + 2)
            for i, amount in enumerate(current):
                if amount > 1.0:          # only excess flows down
                    excess = amount - 1.0
                    half = excess / 2.0
                    next_row[i] += half
                    next_row[i + 1] += half
            current = next_row
        
        # the glass cannot hold more than 1 cup
        return min(1.0, current[query_glass])
