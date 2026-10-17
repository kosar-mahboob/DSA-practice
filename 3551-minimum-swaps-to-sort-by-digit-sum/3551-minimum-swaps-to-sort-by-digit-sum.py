from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
        n = len(nums)
        # target sorted order
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        
        # position map: value -> current index
        pos = {v: i for i, v in enumerate(nums)}
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or nums[i] == target[i]:
                visited[i] = True
                continue
            # traverse cycle
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[target[j]]
                cycle_len += 1
            if cycle_len > 1:
                swaps += cycle_len - 1
        
        return swaps