class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        from typing import List
from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]

        cnt = defaultdict(int)
        ans = 0

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                offset = (r1 - r2, c1 - c2)
                cnt[offset] += 1
                ans = max(ans, cnt[offset])

        return ans