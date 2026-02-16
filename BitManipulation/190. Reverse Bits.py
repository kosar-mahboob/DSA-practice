'''
190. Reverse Bits
Reverse bits of a given 32 bits signed integer.
Example 1:

Input: n = 43261596

Output: 964176192

Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
Example 2:
Input: n = 2147483644
Output: 1073741822
Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
Constraints:
0 <= n <= 231 - 2
n is even.
Follow up: If this function is called many times, how would you optimize it?
'''
class Solution:
    def __init__(self):
        # Precompute reversed byte lookup table
        self._lookup = [self._reverse_byte(i) for i in range(256)]

    def _reverse_byte(self, b):
        # Reverse bits in a single byte
        result = 0
        for i in range(8):
            result |= ((b >> i) & 1) << (7 - i)
        return result

    def reverseBits(self, n: int) -> int:
        # Split 32-bit number into 4 bytes, reverse each, and reassemble in reverse order
        return (self._lookup[(n >> 24) & 0xFF]        | 
                (self._lookup[(n >> 16) & 0xFF] << 8) |
                (self._lookup[(n >> 8) & 0xFF] << 16) |
                (self._lookup[n & 0xFF] << 24))
