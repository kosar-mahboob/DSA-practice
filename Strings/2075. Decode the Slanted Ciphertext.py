class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        if rows == 0 or n == 0:
            return ""
        cols = n // rows
        # Build result by traversing diagonals starting from top row
        res = []
        for j in range(cols):
            i = 0
            while i < rows and j + i < cols:
                pos = i * cols + (j + i)
                res.append(encodedText[pos])
                i += 1
        # Remove trailing spaces (padding)
        return ''.join(res).rstrip()
