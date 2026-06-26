class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # Find positions where target occurs
        positions = [i for i, x in enumerate(nums) if x == target]
        p = len(positions)
        if p == 0:
            return 0
        
        # Convert to +1/-1 array: target = +1, others = -1
        arr = [1 if x == target else -1 for x in nums]
        
        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        vals = sorted(set(prefix))
        size = len(vals)
        bit = [0] * (size + 2)
        
        def update(idx, delta):
            idx += 1
            while idx <= size:
                bit[idx] += delta
                idx += idx & -idx
        
        def query(idx):
            # sum of counts for values <= idx
            idx += 1
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s
        
        ans = 0
        # Add prefix[0] before processing
        idx0 = {v: i for i, v in enumerate(vals)}
        update(idx0[prefix[0]], 1)
        
        for r in range(1, n + 1):
            # Need pref[i] < pref[r]  =>  query(idx(pref[r]) - 1) gives count of prefixes < pref[r]
            idx = idx0[prefix[r]]
            ans += query(idx - 1)
            update(idx, 1)
        
        return ans