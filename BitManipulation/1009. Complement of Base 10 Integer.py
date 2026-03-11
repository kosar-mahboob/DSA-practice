class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        # Create a mask with all bits set for the bit length of n
        mask = (1 << n.bit_length()) - 1
        return n ^ mask
