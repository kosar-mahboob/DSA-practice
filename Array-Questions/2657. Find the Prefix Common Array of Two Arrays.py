from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)   # values are 1..n
        common = 0
        ans = []

        for i in range(n):
            # Process A[i]
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common += 1
            # Process B[i]
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common += 1
            ans.append(common)

        return ans
