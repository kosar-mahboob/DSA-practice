class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Recursive helper
        if n == 1:
            return '0'
        mid = 1 << (n - 1)          # 2^(n-1) is the middle position (1-indexed)
        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # k > mid
            offset = k - mid
            prev_len = (1 << (n - 1)) - 1   # length of S_{n-1}
            # position in the first half (but reversed)
            pos = prev_len - offset + 1
            bit = self.findKthBit(n - 1, pos)
            # invert
            return '1' if bit == '0' else '0'
