class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        maxN = max(zero, one)
        # comp[n][k] = number of compositions of n into k positive integers each <= limit
        comp = [[0] * (maxN + 1) for _ in range(maxN + 1)]
        comp[0][0] = 1
        for n in range(1, maxN + 1):
            for k in range(1, n + 1):
                total = 0
                # last part can be 1 .. min(limit, n)
                for t in range(1, min(limit, n) + 1):
                    total = (total + comp[n - t][k - 1]) % MOD
                comp[n][k] = total

        ans = 0
        for r0 in range(1, zero + 1):
            for r1 in range(1, one + 1):
                if abs(r0 - r1) <= 1:
                    ways = (comp[zero][r0] * comp[one][r1]) % MOD
                    if r0 == r1:
                        ans = (ans + 2 * ways) % MOD
                    else:
                        ans = (ans + ways) % MOD
        return ans
