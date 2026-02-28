class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        length = 1  # current bit length for numbers
        for i in range(1, n + 1):
            if i == (1 << length):   # next power of two reached
                length += 1
            ans = (ans * (1 << length) + i) % MOD
        return ans
