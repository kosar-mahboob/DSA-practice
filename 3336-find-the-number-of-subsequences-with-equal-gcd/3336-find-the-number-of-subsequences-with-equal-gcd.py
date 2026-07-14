class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        max_val = 200
        
        # dp[i][g1][g2] = number of ways to process first i elements
        # with gcd of seq1 = g1 and gcd of seq2 = g2
        # We'll use dictionary to store non-zero states
        dp = defaultdict(int)
        dp[(0, 0)] = 1  # empty subsequences
        
        for x in nums:
            new_dp = defaultdict(int)
            for (g1, g2), count in dp.items():
                # Option 1: skip x
                new_dp[(g1, g2)] = (new_dp[(g1, g2)] + count) % MOD
                
                # Option 2: add x to seq1
                ng1 = gcd(g1, x) if g1 != 0 else x
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)] + count) % MOD
                
                # Option 3: add x to seq2
                ng2 = gcd(g2, x) if g2 != 0 else x
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + count) % MOD
            
            dp = new_dp
        
        # Sum all states where g1 == g2 and both non-empty
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 != 0:
                ans = (ans + count) % MOD
        
        return ans