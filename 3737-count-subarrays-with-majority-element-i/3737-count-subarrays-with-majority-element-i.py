class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        # Convert to +1/-1 array where target = +1, others = -1
        arr = [1 if x == target else -1 for x in nums]
        
        # Prefix sum + count map
        prefix = 0
        count = defaultdict(int)
        count[0] = 1  # empty prefix for subarrays starting at 0
        ans = 0
        
        for x in arr:
            prefix += x
        
        # Simpler O(n^2) solution for n ≤ 1000
        ans = 0
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1
                length = j - i + 1
                if cnt * 2 > length:
                    ans += 1
        return ans