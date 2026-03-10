class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        maxN = max(zero, one)
        # factorials up to maxN
        fact = [1] * (maxN + 1)
        for i in range(1, maxN + 1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact = [1] * (maxN + 1)
        inv_fact[maxN] = pow(fact[maxN], MOD-2, MOD)
        for i in range(maxN, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD

        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        def comp(n, k):
            """number of compositions of n into k positive parts each ≤ limit"""
            if k > n or k * limit < n:
                return 0
            res = 0
            max_j = (n - k) // limit
            for j in range(max_j + 1):
                term = nCr(k, j) * nCr(n - j * limit - 1, k - 1) % MOD
                if j & 1:
                    res = (res - term) % MOD
                else:
                    res = (res + term) % MOD
            return res

        # precompute compositions for zero and one
        comp0 = [0] * (zero + 1)
        for k in range(1, zero + 1):
            comp0[k] = comp(zero, k)
        comp1 = [0] * (one + 1)
        for m in range(1, one + 1):
            comp1[m] = comp(one, m)

        ans = 0
        for k in range(1, zero + 1):
            for m in (k-1, k, k+1):
                if 1 <= m <= one:
                    ways = comp0[k] * comp1[m] % MOD
                    if k == m:
                        ways = ways * 2 % MOD
                    ans = (ans + ways) % MOD
        return ans
