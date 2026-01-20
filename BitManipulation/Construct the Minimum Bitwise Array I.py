# leetcode problem no : 3314. Construct the Minimum Bitwise Array I
from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            val = -1
            for x in range(n):
                if x | (x + 1) == n:
                    val = x
                    break
            ans.append(val)
        return ans
