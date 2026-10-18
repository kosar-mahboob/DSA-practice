from typing import List
from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def count_ways(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            # Ways to interleave left and right sequences
            ways = comb(len(left) + len(right), len(left)) % MOD
            ways = ways * count_ways(left) % MOD
            ways = ways * count_ways(right) % MOD
            return ways

        return (count_ways(nums) - 1) % MOD