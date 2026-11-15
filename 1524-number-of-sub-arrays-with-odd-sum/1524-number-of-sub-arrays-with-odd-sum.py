from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd = even = 0
        cur = 0
        ans = 0
        for x in arr:
            cur ^= x & 1
            if cur:
                ans += even + 1
                odd += 1
            else:
                ans += odd
                even += 1
            ans %= MOD
        return ans