class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
       
        rows = defaultdict(int)
        for r, c in reservedSeats:
            rows[r] |= 1 << c

        total = 2 * (n - len(rows))

        left_mask   = (1<<2)|(1<<3)|(1<<4)|(1<<5)
        middle_mask = (1<<4)|(1<<5)|(1<<6)|(1<<7)
        right_mask  = (1<<6)|(1<<7)|(1<<8)|(1<<9)

        for mask in rows.values():
            left  = (mask & left_mask) == 0
            mid   = (mask & middle_mask) == 0
            right = (mask & right_mask) == 0

            if left and right:
                total += 2
            elif left or mid or right:
                total += 1

        return total