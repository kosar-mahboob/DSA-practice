class Solution:
    def binaryGap(self, n: int) -> int:
        class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Returns the longest distance between two consecutive 1's in the binary
        representation of n. Distance is measured in bit positions (0-indexed from LSB).
        If fewer than two 1's exist, returns 0.
        """
        prev = None          # position of the most recent 1 seen
        pos = 0
        max_dist = 0

        while n:
            if n & 1:        # current least significant bit is 1
                if prev is not None:
                    # distance = current position - previous position
                    max_dist = max(max_dist, pos - prev)
                prev = pos   # update previous position to current
            n >>= 1          # shift right to examine next bit
            pos += 1

        return max_dist
