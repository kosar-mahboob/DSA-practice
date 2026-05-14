from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1  # base[n] has length n+1, so n = max value
        if n <= 0:
            return False
        cnt = [0] * (n + 1)  # indices 1..n
        for x in nums:
            if x < 1 or x > n:
                return False
            cnt[x] += 1
        # Check counts: 1..n-1 exactly once, n exactly twice
        for i in range(1, n):
            if cnt[i] != 1:
                return False
        return cnt[n] == 2
