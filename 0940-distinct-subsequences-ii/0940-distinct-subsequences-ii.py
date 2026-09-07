class Solution:
    def distinctSubseqII(self, s: str) -> int:
      
        MOD = 10**9 + 7
        last = [0] * 26
        dp = 1  # empty subsequence

        for ch in s:
            idx = ord(ch) - 97
            old = dp
            dp = (dp * 2 - last[idx]) % MOD
            last[idx] = old

        return (dp - 1) % MOD